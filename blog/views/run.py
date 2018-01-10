"""
File name: run.py

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
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from blog.models import Run, Chip
from blog.forms import RunForm


def run_list(request):
    """
    Run_list function docstring.

    This function shows the list of runs that are stored in this web app and they are ordered by
    creation date.

    @param request: HTML request page.

    @return: list of runs.
    """
    runs = Run.objects.filter(created_date__lte=timezone.now()).order_by('created_date').reverse()

    return render(request, 'blog/run_list.html', {'runs': runs})


def run_detail(request, pk):
    """
    Run_detail function docstring.

    This function shows the information of a run. BUT THIS FUNCTION IS NOT IN USE NOW.

    @param request: HTML request page.

    @param pk: primary key of the run.

    @return: one run.

    @raise 404: run does not exists.
    """
    run = get_object_or_404(Run, pk=pk)

    return render(request, 'blog/run_detail.html', {'run': run})


@login_required
def run_new(request):
    """
    Run_new function docstring.

    This function shows the form to create a new run. BUT THIS FUNCTION IS NOT IN USE NOW.

    @param request: HTML request page.

    @return: First time, this shows the form to a new run. If the form is completed, return
    the details of this new run.
    """
    if request.method == "POST":
        form = RunForm(request.POST)
        if form.is_valid():
            run = form.save(commit=False)
            run.save()
            return redirect('blog:run_detail', pk=run.pk)
    else:
        form = RunForm()
    return render(request, 'blog/run_edit.html', {'form': form})


@login_required
def run_edit(request, pk):
    """
    Run_edit function docstring.

    This function shows the form to modify a run. BUT THIS FUNCTION IS NOT IN USE NOW.

    @param request: HTML request page.

    @param pk: primary key of the run to modify.

    @return: First time, this shows the form to edit the run information. If the form is
    completed, return the details of this run.

    @raise 404: run does not exists.
    """
    run = get_object_or_404(Run, pk=pk)
    if request.method == "POST":
        form = RunForm(data=request.POST, instance=run)
        if form.is_valid():
            run = form.save(commit=False)
            run.save()
            return redirect('blog:run_detail', pk=run.pk)
    else:
        form = RunForm(instance=run)
    return render(request, 'blog/run_edit.html', {'form': form})


@login_required
def run_remove(request, pk):
    """
    Run_remove function docstring.

    This function removes a run. BUT THIS FUNCTION IS NOT IN USE NOW.

    @param request: HTML request page.

    @param pk: primary key of the run to remove.

    @return: list of runs.

    @raise 404: run does not exists.
    """
    run = get_object_or_404(Run, pk=pk)
    run.delete()
    return redirect('blog:run_list')


def run_chip_list(request, pk):
    """
    Run_chip_list function docstring.

    This function shows the list of chips of a run that are stored in this web app.

    @param request: HTML request page.

    @param pk: primary key of the run.

    @return: list of chips.
    """
    # chips = Chip.objects.filter(run=pk)
    chips = Chip.objects.filter(wafer=pk)

    return render(request, 'blog/chip_list.html', {'chips': chips})
