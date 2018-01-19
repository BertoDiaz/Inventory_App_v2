"""
File name: electronic.py.

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
from blog.models import Electronic, Type_Component, Location
from blog.forms import ElectronicForm
from blog.views.search import get_query


def electronic_list_type_components(request):
    """
    electronic_list_type_components function docstring.

    This function shows the list of type components that are stored in this web app and
    they are ordered by creation date.

    @param request: HTML request page.

    @return: list of type components.
    """
    # electronics = Electronic.objects.filter(
    #     created_date__lte=timezone.now()).order_by('created_date').reverse()

    electronics = Type_Component.objects.all()

    return render(request, 'blog/electronic_list_type_components.html',
                  {'electronics': electronics})


@login_required
def electronic_list(request, pk):
    """
    Electronic_list function docstring.

    This function shows the list of electronic components that are stored in this web app and
    they are ordered by creation date.

    @param request: HTML request page.
    @param pk: primary key of chemical type.

    @return: list of electronic components.
    """
    type_component = Type_Component.objects.get(pk=pk)
    electronic_list = Electronic.objects.filter(
        type_component=type_component).order_by('name_component')

    # Show 25 contacts per page
    paginator = Paginator(electronic_list, 25)

    page = request.GET.get('page')
    try:
        electronics = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        electronics = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        electronics = paginator.page(paginator.num_pages)

    componentsBack = True
    type_componBack = False

    return render(request, 'blog/electronic_list.html', {'electronics': electronics,
                                                         'componentsBack': componentsBack,
                                                         'type_componBack': type_componBack})


@login_required
def electronic_search(request):
    """
    Electronic_search function docstring.

    This function search the electronic components that are stored in this web app and they are
    ordered by name.

    @param request: HTML request page.

    @return: list of electronic components.
    """
    query_string = ''
    found_entries = None
    if ('searchfield' in request.GET) and request.GET['searchfield'].strip():
        query_string = request.GET['searchfield']
        try:
            query_string = Type_Component.objects.get(name=query_string)
            electronic_list = Electronic.objects.filter(type_component=query_string.pk).order_by('name_component')
        except ObjectDoesNotExist:
            try:
                query_string = Location.objects.get(name=query_string)
                electronic_list = Electronic.objects.filter(location=query_string.pk).order_by('name_component')
            except ObjectDoesNotExist:
                entry_query = get_query(query_string, ['name_component', 'value'])
                electronic_list = Electronic.objects.filter(entry_query).order_by('name_component')

    # Show 25 contacts per page
    paginator = Paginator(electronic_list, 25)

    page = request.GET.get('page')
    try:
        electronics = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        electronics = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        electronics = paginator.page(paginator.num_pages)

    return render(request, 'blog/electronic_list.html', {'electronics': electronics})


@login_required
def electronic_detail(request, pk):
    """
    Electronic_detail function docstring.

    This function shows the information of a electronic component.

    @param request: HTML request page.

    @param pk: primary key of the electronic component.

    @return: one electronic component.

    @raise 404: electronic component does not exists.
    """
    electronic = get_object_or_404(Electronic, pk=pk)
    componentsBack = False
    type_componBack = True

    return render(request, 'blog/electronic_detail.html', {'electronic': electronic,
                                                           'componentsBack': componentsBack,
                                                           'type_componBack': type_componBack})


@login_required
def electronic_new(request):
    """
    Electronic_new function docstring.

    This function shows the form to create a new electronic component.

    @param request: HTML request page.

    @return: First time, this shows the form to a new electronic component. If the form is
    completed, return the details of this new electronic component.
    """
    if request.method == "POST":
        form = ElectronicForm(request.POST)
        if form.is_valid():
            electronic = form.save(commit=False)
            electronic_all = Electronic.objects.all()

            duplicates = False

            for data in electronic_all:
                if data.unit == electronic.unit and data.value == electronic.value:
                    duplicates = True
                    electronic_ex = data

            if not duplicates:
                messages.success(request, 'You have added your electronic component successfully.')
                electronic.name_component = electronic.type_component.name
                electronic.save()
            else:
                messages.warning(request, 'Ups!! A electronic component with this value already exists. If you want to add a new to the stock, please edit it.')
                electronic = electronic_ex

            return redirect('blog:electronic_detail', pk=electronic.pk)
    else:
        form = ElectronicForm()
    return render(request, 'blog/electronic_new.html', {'form': form})


@login_required
def electronic_edit(request, pk):
    """
    Electronic_edit function docstring.

    This function shows the form to modify a electronic component.

    @param request: HTML request page.

    @param pk: primary key of the electronic component to modify.

    @return: First time, this shows the form to edit the electronic component information. If the
    form is completed, return the details of this electronic component.

    @raise 404: electronic component does not exists.
    """
    electronic = get_object_or_404(Electronic, pk=pk)
    if request.method == "POST":
        form = ElectronicForm(data=request.POST, instance=electronic)
        if form.is_valid():
            electronic = form.save(commit=False)
            electronic_all = Electronic.objects.all()

            duplicates = False

            for data in electronic_all:
                if data.value == electronic.value and data.unit == electronic.unit:
                    if data.pk != electronic.pk:
                        duplicates = True

            if not duplicates:
                messages.success(request, 'You have updated your electronic component.')
                electronic.save()
                return redirect('blog:electronic_detail', pk=electronic.pk)
            else:
                messages.warning(request, 'Already exists an electronic component with this name.')
                return redirect('blog:electronic_edit', pk=electronic.pk)

    else:
        form = ElectronicForm(instance=electronic)
    return render(request, 'blog/electronic_edit.html', {'form': form})


@login_required
def electronic_remove(request, pk):
    """
    Electronic_remove function docstring.

    This function removes a electronic component.

    @param request: HTML request page.

    @param pk: primary key of the electronic component to remove.

    @return: list of electronic components.

    @raise 404: electronic component does not exists.
    """
    electronic = get_object_or_404(Electronic, pk=pk)
    name_component = electronic.name_component
    electronic.delete()
    return redirect('blog:electronic_list', component=name_component)
