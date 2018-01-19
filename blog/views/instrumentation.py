"""
File name: instrumentation.py.

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
from blog.models import Instrumentation, Type_Instrumentation, Supplier, Location
from blog.forms import InstrumentationForm


def instrumentation_list_type(request):
    """
    Instrumentation_list_type function docstring.

    This function shows the list of instrument types that are stored in this web app and they are
    ordered by creation date.

    @param request: HTML request page.

    @return: list of instrument types.
    """
    instrumentations = Type_Instrumentation.objects.all()

    return render(request, 'blog/instrumentation_list_type.html',
                  {'instrumentations': instrumentations})


@login_required
def instrumentation_list(request, pk):
    """
    Instrumentation_list function docstring.

    This function shows the list of instruments that are stored in this web app and they are
    ordered by creation date.

    @param request: HTML request page.
    @param pk: primary key of instrument types..

    @return: list of instrument types.
    """
    type_instrumentation = Type_Instrumentation.objects.get(pk=pk)
    instrumentation_list = Instrumentation.objects.filter(
        type_instrumentation=type_instrumentation).order_by('characteristics')

    # Show 25 contacts per page
    paginator = Paginator(instrumentation_list, 10)

    page = request.GET.get('page')
    try:
        instrumentations = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        instrumentations = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        instrumentations = paginator.page(paginator.num_pages)

    instrumentBack = True
    type_instrumBack = False

    return render(request, 'blog/instrumentation_list.html', {'instrumentations': instrumentations,
                                                              'instrumentBack': instrumentBack,
                                                              'type_instrumBack': type_instrumBack})


@login_required
def instrumentation_search(request):
    """
    Instrumentation_search function docstring.

    This function search the instruments that are stored in this web app and they are
    ordered by name.

    @param request: HTML request page.

    @return: list of instruments.
    """
    query_string = ''
    found_entries = None
    if ('searchfield' in request.GET) and request.GET['searchfield'].strip():
        query_string = request.GET['searchfield']
        try:
            query_string = Type_Instrumentation.objects.get(name=query_string)
            instrumentation_list = Instrumentation.objects.filter(type_instrumentation=query_string.pk).order_by('type_instrumentation')
        except ObjectDoesNotExist:
            try:
                query_string = Supplier.objects.get(name=query_string)
                instrumentation_list = Instrumentation.objects.filter(supplier=query_string.pk).order_by('type_instrumentation')
            except ObjectDoesNotExist:
                try:
                    query_string = Location.objects.get(name=query_string)
                    instrumentation_list = Instrumentation.objects.filter(location=query_string.pk).order_by('type_instrumentation')
                except ObjectDoesNotExist:
                    entry_query = get_query(query_string, ['characteristics', 'manufacturer'])
                    instrumentation_list = Instrumentation.objects.filter(entry_query).order_by('type_instrumentation')

    # Show 25 contacts per page
    paginator = Paginator(instrumentation_list, 25)

    page = request.GET.get('page')
    try:
        instrumentations = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        instrumentations = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        instrumentations = paginator.page(paginator.num_pages)

    return render(request, 'blog/instrumentation_list.html', {'instrumentations': instrumentations})


@login_required
def instrumentation_detail(request, pk):
    """
    Instrumentation_detail function docstring.

    This function shows the information of a instrument.

    @param request: HTML request page.

    @param pk: primary key of the instrument.

    @return: one instrument.

    @raise 404: instrument does not exists.
    """
    instrumentation = get_object_or_404(Instrumentation, pk=pk)
    instrumentBack = False
    type_instrumBack = True

    return render(request, 'blog/instrumentation_detail.html', {'instrumentation': instrumentation,
                                                                'instrumentBack': instrumentBack,
                                                                'type_instrumBack': type_instrumBack
                                                                })


@login_required
def instrumentation_new(request):
    """
    Instrumentation_new function docstring.

    This function shows the form to create a new instrument.

    @param request: HTML request page.

    @return: First time, this shows the form to a new instrument. If the form is completed, return
    the details of this new instrument.
    """
    if request.method == "POST":
        form = InstrumentationForm(request.POST)
        if form.is_valid():
            instrumentation = form.save(commit=False)
            instrumentation_all = Instrumentation.objects.all()

            duplicates = False

            for data in instrumentation_all:
                if data.characteristics == instrumentation.characteristics:
                    duplicates = True
                    instrumentation_ex = data

            if not duplicates:
                messages.success(request, 'You have added your instrument successfully.')
                instrumentation.save()
            else:
                messages.warning(request, 'Ups!! A instrument with these characteristics already exists. If you want to add a new to the stock, please edit it.')
                instrumentation = instrumentation_ex

            return redirect('blog:instrumentation_detail', pk=instrumentation.pk)
    else:
        form = InstrumentationForm()
    return render(request, 'blog/instrumentation_new.html', {'form': form})


@login_required
def instrumentation_edit(request, pk):
    """
    Instrumentation_edit function docstring.

    This function shows the form to modify a instrument.

    @param request: HTML request page.

    @param pk: primary key of the instrument to modify.

    @return: First time, this shows the form to edit the instrument information. If the form is
    completed, return the details of this instrument.

    @raise 404: instrument does not exists.
    """
    instrumentation = get_object_or_404(Instrumentation, pk=pk)
    if request.method == "POST":
        form = InstrumentationForm(data=request.POST, instance=instrumentation)
        if form.is_valid():
            instrumentation = form.save(commit=False)
            instrumentation_all = Instrumentation.objects.all()

            duplicates = False

            for data in instrumentation_all:
                if data.characteristics == instrumentation.characteristics:
                    if data.pk != instrumentation.pk:
                        duplicates = True

            if not duplicates:
                messages.success(request, 'You have updated your instrumentation.')
                instrumentation.save()
                return redirect('blog:instrumentation_detail', pk=instrumentation.pk)
            else:
                messages.warning(request, 'Already exists an instrumentation with this name.')
                return redirect('blog:instrumentation_edit', pk=instrumentation.pk)

    else:
        form = InstrumentationForm(instance=instrumentation)
    return render(request, 'blog/instrumentation_edit.html', {'form': form})


@login_required
def instrumentation_remove(request, pk):
    """
    Instrumentation_remove function docstring.

    This function removes a instrument.

    @param request: HTML request page.

    @param pk: primary key of the instrument to remove.

    @return: list of instruments.

    @raise 404: instrument does not exists.
    """
    instrumentation = get_object_or_404(Instrumentation, pk=pk)
    instrumentation.delete()
    return redirect('blog:instrumentation_list')
