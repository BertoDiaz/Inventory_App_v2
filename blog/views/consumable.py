"""consumable.py."""

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import Consumable
from blog.forms import ConsumableForm


def consumable_list(request):
    """
    Consumable_list function docstring.

    This function shows the list of consumables that are stored in this web app and they are
    ordered by creation date.

    @param request: HTML request page.

    @return: list of consumables.
    """
    consumables = Consumable.objects.all().order_by('name')
    consumableBack = False
    # type_instrumBack = False

    return render(request, 'blog/consumable_list.html', {'consumables': consumables,
                                                         'consumableBack': consumableBack})


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


@login_required
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
            consumable.save()
            return redirect('blog:consumable_detail', pk=consumable.pk)
    else:
        form = ConsumableForm()
    return render(request, 'blog/consumable_new.html', {'form': form})


@login_required
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


@login_required
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
