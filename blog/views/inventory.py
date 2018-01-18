"""
File name: inventory.py

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
from django.contrib.auth.decorators import login_required
from blog.models import Inventory
from blog.forms import InventoryForm


@login_required
def inventory_list(request):
    """
    Inventory_list function docstring.

    This function shows the different inventories of this web app that are ordered by creation date.

    @param request: HTML request page.

    @return: list of inventories.
    """
    inventories = Inventory.objects.all().order_by('created_date').reverse()

    return render(request, 'blog/inventory_list.html', {'inventories': inventories})


@login_required
def inventory_detail(request, pk):
    """
    Inventory_detail function docstring.

    This function shows the information of an inventory.

    @param request: HTML request page.

    @param pk: primary key of the inventory.

    @return: one inventory.

    @raise 404: inventory does not exists.
    """
    inventory = get_object_or_404(Inventory, pk=pk)

    return render(request, 'blog/inventory_detail.html', {'inventory': inventory})


@login_required
def inventory_new(request):
    """
    Inventory_new function docstring.

    This function shows the form to create a new inventory.

    @param request: HTML request page.

    @return: First time, this shows the form to a new inventory. If the form is completed, return
    the details of this new inventory.
    """
    if request.method == "POST":
        form = InventoryForm(request.POST)
        if form.is_valid():
            inventory = form.save(commit=False)
            inventory.author = request.user
            # inventory.published_date = timezone.now()
            inventory.save()
            return redirect('blog:inventory_detail', pk=inventory.pk)
    else:
        form = InventoryForm()
    return render(request, 'blog/inventory_edit.html', {'form': form})


@login_required
def inventory_edit(request, pk):
    """
    Inventory_edit function docstring.

    This function shows the form to modify an inventory.

    @param request: HTML request page.

    @param pk: primary key of the inventory to modify.

    @return: First time, this shows the form to edit the inventory. If the form is completed, return
    the details of this inventory.

    @raise 404: inventory does not exists.
    """
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == "POST":
        form = InventoryForm(data=request.POST, instance=inventory)
        if form.is_valid():
            inventory = form.save(commit=False)
            inventory.author = request.user
            inventory.save()
            return redirect('blog:inventory_detail', pk=inventory.pk)
    else:
        form = InventoryForm(instance=inventory)
    return render(request, 'blog/inventory_edit.html', {'form': form})


@login_required
def inventory_remove(request, pk):
    """
    Inventory_remove function docstring.

    This function removes an inventory.

    @param request: HTML request page.

    @param pk: primary key of the inventory to remove.

    @return: list of inventories.

    @raise 404: inventory does not exists.
    """
    inventory = get_object_or_404(Inventory, pk=pk)
    inventory.delete()
    return redirect('blog:inventory_list')
