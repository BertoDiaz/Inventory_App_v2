"""
File name: biological.py.

Name: Inventory App

Description: With this web application you can do the inventory of all
             the material of your laboratory or business. You can also
             place orders but this form is case-specific. Moreover,
             you can track all your manufacturing procedures such as
             wafer fabrication in this case.

Copyright (C) 2017  Heriberto J. Díaz Luis-Ravelo

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see http://www.gnu.org/licenses/.

Email: heriberto.diazluis@gmail.com
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from blog.views.search import get_query
from blog.models import Biological, Type_Biological_1, Type_Biological_2, Supplier, Location
from blog.forms import BiologicalForm


def biological_list_type_biological(request):
    """
    biological_list_type_biological function docstring.

    This function shows the list of type of biologicals that are stored in this web app and they are
    ordered by creation date.

    @param request: HTML request page.

    @return: list of type of biologicals.
    """
    biologicals = Type_Biological_1.objects.all()

    biologicals_2 = []

    for biological in biologicals:
        data = Type_Biological_2.objects.filter(type_biological_1=biological)
        biologicals_2.append(data)

    # for bios in biologicals_2:
    #     for bio in bios:
    #         print(bio.type_biological_1)

    return render(request, 'blog/biological_list_type_biological.html',
                  {'biologicals': biologicals, 'biologicals_2': biologicals_2})


@login_required
def biological_list(request, pk):
    """
    Biological_list function docstring.

    This function shows the list of biologicals that are stored in this web app and they are
    ordered by creation date.

    @param request: HTML request page.
    @param pk: primary key of biological types.

    @return: list of biological types.
    """
    type_biological_2 = Type_Biological_2.objects.get(pk=pk)
    biological_list = Biological.objects.filter(type_biological=type_biological_2).order_by('name')

    # Show 25 contacts per page
    paginator = Paginator(biological_list, 10)

    page = request.GET.get('page')
    try:
        biologicals = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        biologicals = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        biologicals = paginator.page(paginator.num_pages)

    biologicalsBack = True
    type_bioBack = False

    return render(request, 'blog/biological_list.html', {'biologicals': biologicals,
                                                         'biologicalsBack': biologicalsBack,
                                                         'type_bioBack': type_bioBack})


@login_required
def biological_search(request):
    """
    Biological_search function docstring.

    This function search the biologicals that are stored in this web app and they are
    ordered by name.

    @param request: HTML request page.

    @return: list of biologicals.
    """
    query_string = ''
    found_entries = None
    if ('searchfield' in request.GET) and request.GET['searchfield'].strip():
        query_string = request.GET['searchfield']
        try:
            query_string = Type_Biological_2.objects.get(name=query_string)
            biological_list = Biological.objects.filter(type_biological=query_string.pk).order_by('name')
        except ObjectDoesNotExist:
            try:
                query_string = Supplier.objects.get(name=query_string)
                biological_list = Biological.objects.filter(supplier=query_string.pk).order_by('name')
            except ObjectDoesNotExist:
                try:
                    query_string = Location.objects.get(name=query_string)
                    biological_list = Biological.objects.filter(location=query_string.pk).order_by('name')
                except ObjectDoesNotExist:
                    entry_query = get_query(query_string, ['name', 'reference', 'quantity'])
                    biological_list = Biological.objects.filter(entry_query).order_by('name')

    # Show 25 contacts per page
    paginator = Paginator(biological_list, 25)

    page = request.GET.get('page')
    try:
        biologicals = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        biologicals = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        biologicals = paginator.page(paginator.num_pages)

    return render(request, 'blog/biological_list.html', {'biologicals': biologicals})


@login_required
def biological_detail(request, pk):
    """
    Biological_detail function docstring.

    This function shows the information of a biological.

    @param request: HTML request page.

    @param pk: primary key of the biological.

    @return: one biological.

    @raise 404: biological does not exists.
    """
    biological = get_object_or_404(Biological, pk=pk)
    biologicalsBack = False
    type_bioBack = True

    return render(request, 'blog/biological_detail.html', {'biological': biological,
                                                           'biologicalsBack': biologicalsBack,
                                                           'type_bioBack': type_bioBack})


@login_required
def biological_new(request):
    """
    Biological_new function docstring.

    This function shows the form to create a new biological.

    @param request: HTML request page.

    @return: First time, this shows the form to a new biological. If the form is completed, return
    the details of this new biological.
    """
    if request.method == "POST":
        form = BiologicalForm(request.POST)
        if form.is_valid():
            biological = form.save(commit=False)
            biological.author = request.user
            biological_all = Biological.objects.all()

            duplicates = False

            for data in biological_all:
                if data.reference == biological.reference:
                    duplicates = True
                    biological_ex = data

            if not duplicates:
                messages.success(request, 'You have added your biological successfully.')
                biological.save()
            else:
                messages.warning(request, 'Ups!! A biological with this reference already exists. If you want to add a new bottle to the stock, please edit it.')
                biological = biological_ex

            return redirect('blog:biological_detail', pk=biological.pk)

    else:
        form = BiologicalForm()
    return render(request, 'blog/biological_new.html', {'form': form})


@login_required
def biological_edit(request, pk):
    """
    Biological_edit function docstring.

    This function shows the form to modify a biological.

    @param request: HTML request page.

    @param pk: primary key of the biological to modify.

    @return: First time, this shows the form to edit the biological information. If the form is
    completed, return the details of this biological.

    @raise 404: biological does not exists.
    """
    biological = get_object_or_404(Biological, pk=pk)
    if request.method == "POST":
        form = BiologicalForm(data=request.POST, instance=biological)
        if form.is_valid():
            biological = form.save(commit=False)
            biological.author = request.user
            biological_all = Biological.objects.all()

            duplicates = False

            for data in biological_all:
                if data.name == biological.name and data.pk != biological.pk:
                    duplicates = True

            if not duplicates:
                messages.success(request, 'You have updated your biological.')
                biological.save()
                return redirect('blog:biological_detail', pk=biological.pk)
            else:
                messages.warning(request, 'Already exists an biological with this name.')
                return redirect('blog:biological_edit', pk=biological.pk)

    else:
        form = BiologicalForm(instance=biological)
    return render(request, 'blog/biological_edit.html', {'form': form})


@login_required
def biological_remove(request, pk):
    """
    Biological_remove function docstring.

    This function removes a biological.

    @param request: HTML request page.

    @param pk: primary key of the biological to remove.

    @return: list of biologicals.

    @raise 404: biological does not exists.
    """
    biological = get_object_or_404(Biological, pk=pk)
    biological.delete()
    return redirect('blog:biological_list')
