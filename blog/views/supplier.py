"""
File name: supplier.py.

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
from blog.models import Supplier
from blog.forms import SupplierForm, ChemicalForm


@login_required
def supplier_list(request):
    """
    Supplier_list function docstring.

    This function shows the list of suppliers that are stored in this web app and they are
    ordered by creation date.

    @param request: HTML request page.

    @return: list of suppliers.
    """
    if request.user.is_staff:
        supplier_list = Supplier.objects.filter(order_show=False).order_by('name')

        # Show 25 contacts per page
        paginator = Paginator(supplier_list, 25)

        page = request.GET.get('page')
        try:
            suppliers = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            suppliers = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            suppliers = paginator.page(paginator.num_pages)

        return render(request, 'blog/supplier_list.html', {'suppliers': suppliers})

    else:
        messages.warning(request, 'Ups!! You do not have privileges.')

    return render(request, 'blog/supplier_list.html')


word_to_search = None


@login_required
def supplier_search(request):
    """
    Supplier_search function docstring.

    This function search the suppliers that are stored in this web app and they are
    ordered by name.

    @param request: HTML request page.

    @return: list of suppliers.
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
            entry_query = get_query(query_string, ['name', 'attention', 'address', 'city_postCode',
                                                   'phone', 'fax', 'email'])
            supplier_list = Supplier.objects.filter(entry_query).order_by('name')
        except ObjectDoesNotExist:
            messages.warning(request, 'I am sorry! I have not found any supplier with this word.')

    # Show 25 contacts per page
    paginator = Paginator(supplier_list, 25)

    try:
        suppliers = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        suppliers = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        suppliers = paginator.page(paginator.num_pages)

    return render(request, 'blog/supplier_list.html', {'suppliers': suppliers})


@login_required
def supplier_detail(request, pk):
    """
    Supplier_detail function docstring.

    This function shows the information of a supplier.

    @param request: HTML request page.

    @param pk: primary key of the supplier.

    @return: one supplier.

    @raise 404: supplier does not exists.
    """
    supplier = get_object_or_404(Supplier, pk=pk)

    backList = True

    return render(request, 'blog/supplier_detail.html', {'supplier': supplier,
                                                         'backList': backList})


@login_required
def supplier_new(request):
    """
    Supplier_new function docstring.

    This function shows the form to create a new supplier.

    @param request: HTML request page.

    @param privi: indicateif the username have privileges.

    @return: First time, this shows the form to a new supplier. If the form is completed, return the
    details of this new supplier.
    """
    if request.method == "POST":
        form = SupplierForm(request.POST)
        if form.is_valid():
            supplier = form.save(commit=False)
            supplier.author = request.user
            supplier_all = Supplier.objects.all()

            duplicates = False

            for data in supplier_all:
                if data.name == supplier.name:
                    duplicates = True
                    supplier_ex = data

            if not duplicates:
                messages.success(request, 'You have added your supplier successfully.')
                supplier.save()
            else:
                messages.warning(request,
                                 'Ups!! A supplier with this name already exists. If you want to do any change, '
                                 'please edit it.')
                supplier = supplier_ex

            return redirect('blog:supplier_detail', pk=supplier.pk)
    else:
        form = SupplierForm()
    return render(request, 'blog/supplier_new.html', {'form': form})


@login_required
def supplier_edit(request, pk):
    """
    Supplier_edit function docstring.

    This function shows the form to modify a supplier.

    @param request: HTML request page.

    @param pk: primary key of the supplier to modify.

    @return: First time, this shows the form to edit the supplier information. If the form is
    completed, return the details of this supplier.

    @raise 404: supplier does not exists.
    """
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == "POST":
        supplier_form = SupplierForm(data=request.POST, instance=supplier)
        if supplier_form.is_valid():
            supplier = supplier_form.save(commit=False)
            # supplier.author = request.user
            supplier_all = Supplier.objects.all()

            duplicates = False

            for data in supplier_all:
                if data.name == supplier.name and data.pk != supplier.pk:
                    duplicates = True

            if not duplicates:
                messages.success(request, 'You have updated your supplier.')
                supplier.save()
                return redirect('blog:supplier_detail', pk=supplier.pk)
            else:
                messages.warning(request, 'Already exists a supplier with this name.')
                return redirect('blog:supplier_edit', pk=supplier.pk)

    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'blog/supplier_edit.html', {'form': form})


@login_required
def supplier_remove(request, pk):
    """
    Supplier_remove function docstring.

    This function removes a supplier.

    @param request: HTML request page.

    @param pk: primary key of the supplier to remove.

    @return: list of suppliers.

    @raise 404: supplier does not exists.
    """
    supplier = get_object_or_404(Supplier, pk=pk)
    supplier.delete()
    return redirect('blog:supplier_list')
