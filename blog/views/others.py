"""
File name: others.py

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
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from blog.models import Others
from blog.forms import OthersForm


@login_required
def others_list(request):
    """
    Others_list function docstring.

    This function shows the list of components whithout type that are stored in this web app and
    they are ordered by creation date.

    @param request: HTML request page.

    @return: list of components whithout type.
    """
    others_list = Others.objects.filter(
        created_date__lte=timezone.now()).order_by('created_date').reverse()

    # Show 25 contacts per page
    paginator = Paginator(others_list, 10)

    page = request.GET.get('page')
    try:
        otherss = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        otherss = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        otherss = paginator.page(paginator.num_pages)

    return render(request, 'blog/others_list.html', {'otherss': otherss})


@login_required
def others_detail(request, pk):
    """
    Others_detail function docstring.

    This function shows the information of a component whithout type.

    @param request: HTML request page.

    @param pk: primary key of the component.

    @return: one components whithout type.

    @raise 404: component does not exists.
    """
    others = get_object_or_404(Others, pk=pk)

    return render(request, 'blog/others_detail.html', {'others': others})


@login_required
def others_new(request):
    """
    Others_new function docstring.

    This function shows the form to create a new component without type.

    @param request: HTML request page.

    @return: First time, this shows the form to a new component. If the form is completed, return
    the details of this new component without type.
    """
    if request.method == "POST":
        form = OthersForm(request.POST)
        if form.is_valid():
            others = form.save(commit=False)
            others.save()
            return redirect('blog:others_detail', pk=others.pk)
    else:
        form = OthersForm()
    return render(request, 'blog/others_edit.html', {'form': form})


@login_required
def others_edit(request, pk):
    """
    Others_edit function docstring.

    This function shows the form to modify a component without type.

    @param request: HTML request page.

    @param pk: primary key of the component to modify.

    @return: First time, this shows the form to edit the component information. If the form is
    completed, return the details of this component without type.

    @raise 404: component does not exists.
    """
    others = get_object_or_404(Others, pk=pk)
    if request.method == "POST":
        form = OthersForm(data=request.POST, instance=others)
        if form.is_valid():
            others = form.save(commit=False)
            others.save()
            return redirect('blog:others_detail', pk=others.pk)
    else:
        form = OthersForm(instance=others)
    return render(request, 'blog/others_edit.html', {'form': form})


@login_required
def others_remove(request, pk):
    """
    Others_remove function docstring.

    This function removes a component that does not have type.

    @param request: HTML request page.

    @param pk: primary key of the component to remove.

    @return: list of components.

    @raise 404: component does not exists.
    """
    others = get_object_or_404(Others, pk=pk)
    others.delete()
    return redirect('blog:others_list')
