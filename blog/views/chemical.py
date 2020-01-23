"""
File name: chemical.py.

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
from blog.models import Chemical, Type_Chemical, State, Supplier, Location
from blog.forms import ChemicalForm, SupplierNameForm


def chemical_list_type_chemical(request):
    """
    Chemical_list_type_chemical function docstring.

    This function shows the list of type of chemicals that are stored in this web app and they are
    ordered by creation date.

    @param request: HTML request page.

    @return: list of type of chemicals.
    """
    # states = State.objects.all()
    chemicals = Type_Chemical.objects.all().order_by('name')

    return render(request, 'blog/chemical_list_type_chemical.html', {'chemicals': chemicals})


@login_required(login_url='/accounts/signin/')
def chemical_list(request, pk):
    """
    Chemical_list function docstring.

    This function shows the list of chemicals that are stored in this web app and they are
    ordered by creation date.

    @param request: HTML request page.
    @param pk: primary key of chemical type.

    @return: list of chemicals.
    """
    type_chemical = Type_Chemical.objects.get(pk=pk)
    chemical_list = Chemical.objects.filter(type_chemical=type_chemical).order_by('name', 'quantity')

    # Show 25 contacts per page
    paginator = Paginator(chemical_list, 10)

    page = request.GET.get('page')
    try:
        chemicals = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        chemicals = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        chemicals = paginator.page(paginator.num_pages)

    chemicalsBack = True
    type_chemicalBack = False

    return render(request, 'blog/chemical_list.html', {'chemicals': chemicals,
                                                       'chemicalsBack': chemicalsBack,
                                                       'type_chemicalBack': type_chemicalBack})


word_to_search = None


@login_required(login_url='/accounts/signin/')
def chemical_search(request):
    """
    Chemical_search function docstring.

    This function search the chemicals that are stored in this web app and they are
    ordered by name.

    @param request: HTML request page.

    @return: list of chemicals.
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
            query_string = Type_Chemical.objects.get(name=query_string)
            chemical_list = Chemical.objects.filter(type_chemical=query_string.pk).order_by('name')
        except ObjectDoesNotExist:
            try:
                query_string = State.objects.get(name=query_string)
                chemical_list = Chemical.objects.filter(state=query_string.pk).order_by('name')
            except ObjectDoesNotExist:
                try:
                    query_string = Supplier.objects.get(name=query_string)
                    chemical_list = Chemical.objects.filter(supplier=query_string.pk).order_by('name')
                except ObjectDoesNotExist:
                    try:
                        query_string = Location.objects.get(name=query_string)
                        chemical_list = Chemical.objects.filter(location=query_string.pk).order_by('name')
                    except ObjectDoesNotExist:
                        entry_query = get_query(query_string, ['name', 'molecular_formula', 'reference', 'cas_number',
                                                               'quantity'])
                        chemical_list = Chemical.objects.filter(entry_query).order_by('name')

    # Show 25 contacts per page
    paginator = Paginator(chemical_list, 25)

    try:
        chemicals = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        chemicals = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        chemicals = paginator.page(paginator.num_pages)

    return render(request, 'blog/chemical_list.html', {'chemicals': chemicals})


@login_required(login_url='/accounts/signin/')
def chemical_detail(request, pk):
    """
    Chemical_detail function docstring.

    This function shows the information of a chemical.

    @param request: HTML request page.

    @param pk: primary key of the chemical.

    @return: one chemical.

    @raise 404: chemical does not exists.
    """
    chemical = get_object_or_404(Chemical, pk=pk)
    chemicalsBack = False
    type_chemicalBack = True

    return render(request, 'blog/chemical_detail.html', {'chemical': chemical,
                                                         'chemicalsBack': chemicalsBack,
                                                         'type_chemicalBack': type_chemicalBack})


@login_required(login_url='/accounts/signin/')
def chemical_new(request):
    """
    Chemical_new function docstring.

    This function shows the form to create a new chemical.

    @param request: HTML request page.

    @return: First time, this shows the form to a new chemical. If the form is completed, return
    the details of this new chemical.
    """
    if request.method == "POST":
        form = ChemicalForm(request.POST, prefix="chemical")

        if form.is_valid():
            chemical = form.save(commit=False)
            chemical.author = request.user

            supplier_form = SupplierNameForm(data=request.POST, prefix="supplierNameForm")
            supplier = supplier_form.save(commit=False)

            # if chemical.supplier.name == "SUPPLIER NOT REGISTERED" and not supplier_form.is_valid():
            if chemical.supplier.name == "SUPPLIER NOT REGISTERED" and (supplier.name != "NONE" and
                                                                        supplier.name == ""):

                supplier_form = SupplierNameForm(data=request.POST, prefix="supplierNameForm")
                addSupplier = True

                messages.warning(request,
                                 'You have to write the next information about the supplier. If you do not know how is '
                                 'the supplier, you write NONE.')

                return render(request, 'blog/chemical_new.html', {'form': form,
                                                                  'supplier_form': supplier_form,
                                                                  'addSupplier': addSupplier})

            else:

                if supplier_form.is_valid() and not supplier.name == "NONE" and chemical.supplier.name == "SUPPLIER NOT REGISTERED":

                    duplicates = False

                    supplier_all = Supplier.objects.all()

                    for data in supplier_all:
                        if data.name == supplier.name:
                            duplicates = True
                            supplier_ex = data

                    if not duplicates:
                        supplier.save()

                    else:
                        messages.warning(request, 'It is not necessary to add this supplier because already exists.')
                        addSupplier = False

                        chemical.supplier = supplier_ex

                        form = ChemicalForm(instance=chemical, prefix="chemical")

                        return render(request, 'blog/chemical_new.html', {'form': form,
                                                                          'supplier_form': supplier_form,
                                                                          'addSupplier': addSupplier})

                    chemical.supplier = supplier

                if chemical.reference == "" or chemical.reference == "-":
                    chemical.reference = "-"

                if chemical.cas_number == "" or chemical.cas_number == "-":
                    chemical.cas_number = "-"

                if chemical.number_bottle == "" or chemical.number_bottle == "-":
                    chemical.number_bottle = "-"

                if chemical.quantity == "" or chemical.quantity == "-":
                    chemical.quantity = "-"

                if chemical.molecular_weight == "" or chemical.molecular_weight == "-":
                    chemical.molecular_weight = "-"
                    chemical.unit_chemical = "-"

                else:
                    chemical.unit_chemical = "g/mol"

                if chemical.molecular_formula == "" or chemical.molecular_formula == "-":
                    chemical.molecular_formula = "-"

                chemical_all = Chemical.objects.all()

                duplicates = False

                for data in chemical_all:
                    if (data.reference == chemical.reference) and (chemical.reference != "-"):

                        if (data.pk != chemical.pk):

                            if (data.molecular_weight == chemical.molecular_weight):

                                if (data.quantity == chemical.quantity):
                                    duplicates = True
                                    chemical_ex = data

                    elif (data.name == chemical.name):

                        if (data.pk != chemical.pk):

                            if (data.molecular_weight == chemical.molecular_weight):

                                if (data.quantity == chemical.quantity):
                                    duplicates = True
                                    chemical_ex = data

                if not duplicates:
                    messages.success(request, 'You have added your chemical successfully.')
                    chemical.save()
                else:
                    messages.warning(request,
                                     'Ups!! A chemical with this reference already exists. If you want to add a new '
                                     'bottle to the stock, please edit it.')
                    chemical = chemical_ex

                return redirect('blog:chemical_detail', pk=chemical.pk)

    else:
        form = ChemicalForm(prefix="chemical")
    return render(request, 'blog/chemical_new.html', {'form': form})


@login_required(login_url='/accounts/signin/')
def chemical_edit(request, pk):
    """
    Chemical_edit function docstring.

    This function shows the form to modify a chemical.

    @param request: HTML request page.

    @param pk: primary key of the chemical to modify.

    @return: First time, this shows the form to edit the chemical information. If the form is
    completed, return the details of this chemical.

    @raise 404: chemical does not exists.
    """
    chemical = get_object_or_404(Chemical, pk=pk)

    if request.method == "POST":
        form = ChemicalForm(data=request.POST, instance=chemical)

        if form.is_valid():
            chemical = form.save(commit=False)
            chemical.edited_by = request.user.username

            supplier_form = SupplierNameForm(data=request.POST, prefix="supplierNameForm")
            supplier = supplier_form.save(commit=False)

            # if chemical.supplier.name == "SUPPLIER NOT REGISTERED" and not supplier_form.is_valid():
            if chemical.supplier.name == "SUPPLIER NOT REGISTERED" and (supplier.name != "NONE" and supplier.name == ""):

                supplier_form = SupplierNameForm(data=request.POST, prefix="supplierNameForm")
                addSupplier = True

                messages.warning(request,
                                 'You have to write the next information about the supplier. If you do not know how is '
                                 'the supplier, you write NONE.')

                return render(request, 'blog/chemical_edit.html', {'pk': chemical.pk,
                                                                   'form': form,
                                                                   'supplier_form': supplier_form,
                                                                   'addSupplier': addSupplier})

            else:

                if supplier_form.is_valid() and not supplier.name == "NONE" and chemical.supplier.name == "SUPPLIER NOT REGISTERED":

                    duplicates = False

                    supplier_all = Supplier.objects.all()

                    for data in supplier_all:
                        if data.name == supplier.name:
                            duplicates = True
                            supplier_ex = data

                    if not duplicates:
                        supplier.save()

                    else:
                        messages.warning(request, 'It is not necessary to add this supplier because already exists.')
                        addSupplier = False

                        chemical.supplier = supplier_ex

                        form = ChemicalForm(instance=chemical, prefix="chemical")

                        return render(request, 'blog/chemical_edit.html', {'pk': chemical.pk,
                                                                           'form': form,
                                                                           'supplier_form': supplier_form,
                                                                           'addSupplier': addSupplier})

                    chemical.supplier = supplier

            if chemical.reference == "" or chemical.reference == "-":
                chemical.reference = "-"

            if chemical.cas_number == "" or chemical.cas_number == "-":
                chemical.cas_number = "-"

            if chemical.number_bottle == "" or chemical.number_bottle == "-":
                chemical.number_bottle = "-"

            if chemical.quantity == "" or chemical.quantity == "-":
                chemical.quantity = "-"

            if chemical.molecular_weight == "" or chemical.molecular_weight == "-":
                chemical.molecular_weight = "-"
                chemical.unit_chemical = "-"

            else:
                chemical.unit_chemical = "g/mol"

            if chemical.molecular_formula == "" or chemical.molecular_formula == "-":
                chemical.molecular_formula = "-"

            chemical_all = Chemical.objects.all()

            duplicates = False

            for data in chemical_all:
                if (data.reference == chemical.reference) and (chemical.reference != "-"):

                    if (data.pk != chemical.pk):

                        if (data.molecular_weight == chemical.molecular_weight):

                            if (data.quantity == chemical.quantity):
                                duplicates = True
                                biological_ex = data

                elif (data.name == chemical.name):

                    if (data.pk != chemical.pk):

                        if (data.molecular_weight == chemical.molecular_weight):

                            if (data.quantity == chemical.quantity):
                                duplicates = True
                                biological_ex = data

            if not duplicates:
                messages.success(request, 'You have updated your chemical.')
                chemical.save()
                return redirect('blog:chemical_detail', pk=chemical.pk)
            else:
                messages.warning(request, 'Already exists an chemical with this name.')
                return redirect('blog:chemical_edit', pk=chemical.pk)

    else:
        form = ChemicalForm(instance=chemical)

    return render(request, 'blog/chemical_edit.html', {'form': form})


@login_required(login_url='/accounts/signin/')
def chemical_remove(request, pk):
    """
    Chemical_remove function docstring.

    This function removes a chemical.

    @param request: HTML request page.

    @param pk: primary key of the chemical to remove.

    @return: list of chemicals.

    @raise 404: chemical does not exists.
    """
    chemical = get_object_or_404(Chemical, pk=pk)
    chemical.delete()
    return redirect('blog:chemical_list_type_chemical')


@login_required(login_url='/accounts/signin/')
def chemical_supplierToNotRegistered(request):
    """
    Chemical_list function docstring.

    This function search if the supplier field is empty and change it by SUPPLIER NOT REGISTERED.

    @param request: HTML request page.

    @return: list of types of chemicals.
    """
    chemical_list = Chemical.objects.all().order_by('name')
    supplier = Supplier.objects.get(name='SUPPLIER NOT REGISTERED')

    for chemical in chemical_list:
        if len(chemical.supplier.name) == 0:
            chemical.supplier = supplier
            chemical.save()

    return redirect('blog:chemical_list_type_chemical')
