"""
File name: consumable.py.

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
from blog.models import Consumable, Supplier, Location
from blog.forms import ConsumableForm


@login_required(login_url='/accounts/signin/')
def consumable_list(request):
    """
    Consumable_list function docstring.

    This function shows the list of consumables that are stored in this web app and they are
    ordered by creation date.

    @param request: HTML request page.

    @return: list of consumables.
    """
    consumable_list = Consumable.objects.all().order_by('name')

    # Show 25 contacts per page
    paginator = Paginator(consumable_list, 10)

    page = request.GET.get('page')
    try:
        consumables = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        consumables = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        consumables = paginator.page(paginator.num_pages)

    consumableBack = False
    # type_instrumBack = False

    return render(request, 'blog/consumable_list.html', {'consumables': consumables,
                                                         'consumableBack': consumableBack})


word_to_search = None


@login_required(login_url='/accounts/signin/')
def consumable_search(request):
    """
    Consumable_search function docstring.

    This function search the consumables that are stored in this web app and they are
    ordered by name.

    @param request: HTML request page.

    @return: list of consumables.
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
            query_string = Supplier.objects.get(name=query_string)
            consumable_list = Consumable.objects.filter(supplier=query_string.pk).order_by('name')
        except ObjectDoesNotExist:
            try:
                query_string = Location.objects.get(name=query_string)
                consumable_list = Consumable.objects.filter(location=query_string.pk).order_by('name')
            except ObjectDoesNotExist:
                entry_query = get_query(query_string, ['name', 'characteristics', 'manufacturer'])
                consumable_list = Consumable.objects.filter(entry_query).order_by('name')

    # Show 25 contacts per page
    paginator = Paginator(consumable_list, 25)

    try:
        consumables = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        consumables = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        consumables = paginator.page(paginator.num_pages)

    return render(request, 'blog/consumable_list.html', {'consumables': consumables})


@login_required(login_url='/accounts/signin/')
def consumable_detail(request, pk):
    """
    Consumable_detail function docstring.

    This function shows the information of a consumable.

    @param request: HTML request page.

    @param pk: primary key of the consumable.

    @return: one consumable.

    @raise 404: consumable does not exists.
    """
    consumable = get_object_or_404(Consumable, pk=pk)
    consumableBack = True
    # type_instrumBack = True

    return render(request, 'blog/consumable_detail.html', {'consumable': consumable,
                                                           'consumableBack': consumableBack})


@login_required(login_url='/accounts/signin/')
def consumable_new(request):
    """
    Consumable_new function docstring.

    This function shows the form to create a new consumable.

    @param request: HTML request page.

    @return: First time, this shows the form to a new consumable. If the form is completed, return
    the details of this new consumable.
    """
    if request.method == "POST":
        form = ConsumableForm(request.POST)
        if form.is_valid():
            consumable = form.save(commit=False)
            consumable.author = request.user
            consumable_all = Consumable.objects.all()

            duplicates = False

            for data in consumable_all:
                if data.name == consumable.name:
                    duplicates = True
                    consumable_ex = data

            if not duplicates:
                messages.success(request, 'You have added your consumable successfully.')
                consumable.save()
            else:
                messages.warning(request,
                                 'Ups!! A consumable with this name already exists. If you want to add a new to the '
                                 'stock, please edit it.')
                consumable = consumable_ex

            return redirect('blog:consumable_detail', pk=consumable.pk)
    else:
        form = ConsumableForm()
    return render(request, 'blog/consumable_new.html', {'form': form})


@login_required(login_url='/accounts/signin/')
def consumable_edit(request, pk):
    """
    Consumable_edit function docstring.

    This function shows the form to modify a consumable.

    @param request: HTML request page.

    @param pk: primary key of the consumable to modify.

    @return: First time, this shows the form to edit the consumable information. If the form is
    completed, return the details of this consumable.

    @raise 404: consumable does not exists.
    """
    consumable = get_object_or_404(Consumable, pk=pk)
    if request.method == "POST":
        form = ConsumableForm(data=request.POST, instance=consumable)
        if form.is_valid():
            consumable = form.save(commit=False)
            consumable.author = request.user
            consumable_all = Consumable.objects.all()

            duplicates = False

            for data in consumable_all:
                if data.name == consumable.name and data.pk != consumable.pk:
                    duplicates = True

            if not duplicates:
                messages.success(request, 'You have updated your consumable.')
                consumable.save()
                return redirect('blog:consumable_detail', pk=consumable.pk)
            else:
                messages.warning(request, 'Already exists an consumable with this name.')
                return redirect('blog:consumable_edit', pk=consumable.pk)

    else:
        form = ConsumableForm(instance=consumable)
    return render(request, 'blog/consumable_edit.html', {'form': form})


@login_required(login_url='/accounts/signin/')
def consumable_remove(request, pk):
    """
    Consumable_remove function docstring.

    This function removes a consumable.

    @param request: HTML request page.

    @param pk: primary key of the consumable to remove.

    @return: list of consumables.

    @raise 404: consumable does not exists.
    """
    consumable = get_object_or_404(Consumable, pk=pk)
    consumable.delete()
    return redirect('blog:consumable_list')
