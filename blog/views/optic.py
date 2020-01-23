"""
File name: optic.py.

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
from blog.models import Optic, Type_Optic, Location
from blog.forms import OpticForm
from blog.views.search import get_query


def optic_list_type_optic(request):
    """
    Optic_list_type_optic function docstring.

    This function shows the list of type of optic components that are stored in this web app and
    they are ordered by creation date.

    @param request: HTML request page.

    @return: list of type of optic components.
    """
    optics = Type_Optic.objects.all()

    return render(request, 'blog/optic_list_type_optic.html', {'optics': optics})


@login_required(login_url='/accounts/signin/')
def optic_list(request, pk):
    """
    Optic_list function docstring.

    This function shows the list of optic components that are stored in this web app and
    they are ordered by creation date.

    @param request: HTML request page.
    @param pk: primary key of chemical type.

    @return: list of optic components.
    """
    type_optic = Type_Optic.objects.get(pk=pk)
    optic_list = Optic.objects.filter(type_optic=type_optic).order_by('location')

    # Show 25 contacts per page
    paginator = Paginator(optic_list, 10)

    page = request.GET.get('page')
    try:
        optics = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        optics = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        optics = paginator.page(paginator.num_pages)

    opticsBack = True
    type_opticBack = False

    return render(request, 'blog/optic_list.html', {'optics': optics, 'opticsBack': opticsBack,
                                                    'type_opticBack': type_opticBack})


word_to_search = None


@login_required(login_url='/accounts/signin/')
def optic_search(request):
    """
    Optic_search function docstring.

    This function search the optic components that are stored in this web app and they are
    ordered by name.

    @param request: HTML request page.

    @return: list of optic components.
    """
    global word_to_search
    query_string = ''
    found_entries = None

    page = request.GET.get('page')

    if (('searchfield' in request.GET) and request.GET['searchfield'].strip()) or page is not None:
        if page is not None:
            query_string = word_to_search

        else:
            query_string = request.GET['searchfield']
            word_to_search = query_string

        try:
            query_string = Type_Optic.objects.get(name=query_string)
            optic_list = Optic.objects.filter(type_optic=query_string.pk).order_by('name_optic')
        except ObjectDoesNotExist:
            try:
                query_string = Location.objects.get(name=query_string)
                optic_list = Optic.objects.filter(location=query_string.pk).order_by('name_optic')
            except ObjectDoesNotExist:
                entry_query = get_query(query_string, ['name_optic', 'subtype_optic', 'model',
                                                       'manufacturer', 'description'])
                optic_list = Optic.objects.filter(entry_query).order_by('name_optic')

    # Show 25 contacts per page
    paginator = Paginator(optic_list, 25)

    try:
        optics = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        optics = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        optics = paginator.page(paginator.num_pages)

    return render(request, 'blog/optic_list.html', {'optics': optics})


@login_required(login_url='/accounts/signin/')
def optic_detail(request, pk):
    """
    Optic_detail function docstring.

    This function shows the information of a optic component.

    @param request: HTML request page.

    @param pk: primary key of the optic component.

    @return: one optic component.

    @raise 404: optic component does not exists.
    """
    optic = get_object_or_404(Optic, pk=pk)
    opticsBack = False
    type_opticBack = True

    return render(request, 'blog/optic_detail.html', {'optic': optic, 'opticsBack': opticsBack,
                                                      'type_opticBack': type_opticBack})


@login_required(login_url='/accounts/signin/')
def optic_new(request):
    """
    Optic_new function docstring.

    This function shows the form to create a new optic component.

    @param request: HTML request page.

    @return: First time, this shows the form to a new optic component. If the form is
    completed, return the details of this new optic component.
    """
    if request.method == "POST":
        form = OpticForm(request.POST)

        if form.is_valid():
            optic = form.save(commit=False)
            optic.author = request.user

            optic_all = Optic.objects.all()

            duplicates = False

            for data in optic_all:
                if data.pk == optic.pk:
                    duplicates = True
                    optic_ex = data
                elif data.model == optic.model and data.manufacturer == optic.manufacturer:
                    if data.location == optic.location:
                        duplicates = True
                        optic_ex = data

            if not duplicates:
                messages.success(request, 'You have added your optic component successfully.')
                # optic.name_optic = optic.type_optic.name
                optic.save()
            else:
                messages.warning(request,
                                 'Ups!! A optic component with this description already exists. If you want to add a '
                                 'new to the stock, please edit it.')
                optic = optic_ex

            return redirect('blog:optic_detail', pk=optic.pk)
    else:
        form = OpticForm()
    return render(request, 'blog/optic_new.html', {'form': form})


@login_required(login_url='/accounts/signin/')
def optic_edit(request, pk):
    """
    Optic_edit function docstring.

    This function shows the form to modify a optic component.

    @param request: HTML request page.

    @param pk: primary key of the optic component to modify.

    @return: First time, this shows the form to edit the optic component information. If the
    form is completed, return the details of this optic component.

    @raise 404: optic component does not exists.
    """
    optic = get_object_or_404(Optic, pk=pk)

    if request.method == "POST":
        form = OpticForm(data=request.POST, instance=optic)

        if form.is_valid():
            optic = form.save(commit=False)
            optic.edited_by = request.user.username

            optic_all = Optic.objects.all()

            duplicates = False

            for data in optic_all:
                if data.pk != optic.pk:
                    if (data.model == optic.model) and (data.manufacturer == optic.manufacturer):
                        if data.location == optic.location:
                            duplicates = True
                            optic_ex = data

            if not duplicates:
                messages.success(request, 'You have updated your optic component.')
                optic.save()
                return redirect('blog:optic_detail', pk=optic.pk)
            else:
                messages.warning(request, 'Already exists an optic component with this name.')
                return redirect('blog:optic_edit', pk=optic.pk)
    else:
        form = OpticForm(instance=optic)
    return render(request, 'blog/optic_edit.html', {'form': form})


@login_required(login_url='/accounts/signin/')
def optic_remove(request, pk):
    """
    Optic_remove function docstring.

    This function removes a optic component.

    @param request: HTML request page.

    @param pk: primary key of the optic component to remove.

    @return: list of optic components.

    @raise 404: optic component does not exists.
    """
    optic = get_object_or_404(Optic, pk=pk)
    optic.delete()
    return redirect('blog:optic_list_type_optic')
