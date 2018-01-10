"""
File name: computing.py

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
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Email: heriberto.diazluis@gmail.com
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import Computing
from blog.forms import ComputingForm


def computing_list(request):
    """
    Computing_list function docstring.

    This function shows the list of computers that are stored in this web app and they are
    ordered by creation date.

    @param request: HTML request page.

    @return: list of computers.
    """
    computing_list = Computing.objects.all().order_by('name')

    # Show 25 contacts per page
    paginator = Paginator(computing_list, 25)

    page = request.GET.get('page')
    try:
        computings = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        computings = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        computings = paginator.page(paginator.num_pages)

    return render(request, 'blog/computing_list.html', {'computings': computings})


def computing_detail(request, pk):
    """
    Computing_detail function docstring.

    This function shows the information of a computer.

    @param request: HTML request page.

    @param pk: primary key of the computer.

    @return: one computer.

    @raise 404: computer does not exists.
    """
    computing = get_object_or_404(Computing, pk=pk)

    backList = True

    return render(request, 'blog/computing_detail.html', {'computing': computing,
                                                          'backList': backList})


@login_required
def computing_new(request):
    """
    Computing_new function docstring.

    This function shows the form to create a new computer.

    @param request: HTML request page.

    @return: First time, this shows the form to a new computer. If the form is completed, return the
    details of this new computer.
    """
    if request.method == "POST":
        form = ComputingForm(request.POST)
        if form.is_valid():
            computing = form.save(commit=False)
            computing.save()
            return redirect('blog:computing_detail', pk=computing.pk)
    else:
        form = ComputingForm()
    return render(request, 'blog/computing_new.html', {'form': form})


@login_required
def computing_edit(request, pk):
    """
    Computing_edit function docstring.

    This function shows the form to modify a computer.

    @param request: HTML request page.

    @param pk: primary key of the computer to modify.

    @return: First time, this shows the form to edit the computer information. If the form is
    completed, return the details of this computer.

    @raise 404: computer does not exists.
    """
    computing = get_object_or_404(Computing, pk=pk)
    if request.method == "POST":
        computing_form = ComputingForm(data=request.POST, instance=computing)
        if computing_form.is_valid():
            computing = computing_form.save(commit=False)
            computing_all = Computing.objects.all()

            duplicates = False

            for data in computing_all:
                if data.name == computing.name and data.pk != computing.pk:
                    duplicates = True

            if not duplicates:
                messages.success(request, 'You have updated your computing.')
                computing.save()
                return redirect('blog:computing_detail', pk=computing.pk)
            else:
                messages.warning(request, 'Already exists a computing with this name.')
                return redirect('blog:computing_edit', pk=computing.pk)

    else:
        form = ComputingForm(instance=computing)
    return render(request, 'blog/computing_edit.html', {'form': form})


@login_required
def computing_remove(request, pk):
    """
    Computing_remove function docstring.

    This function removes a computer.

    @param request: HTML request page.

    @param pk: primary key of the computer to remove.

    @return: list of computers.

    @raise 404: computer does not exists.
    """
    computing = get_object_or_404(Computing, pk=pk)
    computing.delete()
    return redirect('blog:computing_list')
