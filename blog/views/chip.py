"""
File name: chip.py.

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
from blog.models import Run, Chip, Wafer, Name_Waveguide
from blog.forms import RunForm, WaferForm, ChipForm, WaveguideForm


@login_required(login_url='/accounts/signin/')
def chip_list(request):
    """
    Chip_list function docstring.

    This function shows the list of chips that are stored in this web app and they are ordered by
    creation date.

    @param request: HTML request page.

    @return: list of chips.
    """
    chips = Chip.objects.filter(created_date__lte=timezone.now()).order_by('created_date')

    return render(request, 'blog/chip_list.html', {'chips': chips})


@login_required(login_url='/accounts/signin/')
def chip_detail(request, pk):
    """
    Chip_detail function docstring.

    This function shows the information of a chip.

    @param request: HTML request page.

    @param pk: primary key of the chip.

    @return: one chip.

    @raise 404: chip does not exists.
    """
    chip = get_object_or_404(Chip, pk=pk)
    runback = False
    waferback = True

    return render(request, 'blog/chip_detail.html', {'chip': chip, 'waferPK': chip.wafer.pk,
                                                     'runback': runback, 'waferback': waferback})


@login_required(login_url='/accounts/signin/')
def chip_detail_exist(request, pk):
    """
    Chip_detail_exist function docstring.

    This function shows the information of a chip when a chip is created but this already exists.

    @param request: HTML request page.

    @param pk: primary key of the chip.

    @return: one chip.

    @raise 404: chip does not exists.
    """
    chip = get_object_or_404(Chip, pk=pk)

    return render(request, 'blog/chip_detail_exist.html', {'chip': chip})


@login_required(login_url='/accounts/signin/')
def chip_new(request):
    """
    Chip_new function docstring.

    This function shows the form to create a new chip. This function uses 3 forms to create a new
    chip (Run form, Wafer form and Chip form), moreover, when the form is completed, this function
    search if the run or wafer or chip already exists.

    @param request: HTML request page.

    @return: First time, this shows the form to a new chip. If the form is completed and the run or
    wafer or chip does not exists, return the details of this new chip.
    """
    if request.method == "POST":
        runForm = RunForm(request.POST, prefix='run')
        waferForm = WaferForm(request.POST, prefix='wafer')
        chipForm = ChipForm(request.POST, prefix='chip')
        # waveguideForm = WaveguideForm(request.POST, prefix='waveguide')
        if runForm.is_valid():
            run = runForm.save(commit=False)
            run_ex = Run.objects.get(run=run.run)
            # print(run)
            if not run_ex:
                # print(run_ex)
                run.save()
            else:
                run = run_ex
        if waferForm.is_valid():
            wafer = waferForm.save(commit=False)
            wafer_ex = Wafer.objects.get(wafer=wafer.wafer, run=run)
            # print(wafer)
            if not wafer_ex:
                # print(wafer_ex)
                wafer.run = run
                wafer.save()
            else:
                wafer = wafer_ex
        if chipForm.is_valid():
            chip = chipForm.save(commit=False)
            chip_ex = Chip.objects.get(chip=chip.chip, wafer=wafer, run=run)
            # print(chip)
            if not chip_ex:
                # print(chip_ex)
                chip.run = run
                chip.wafer = wafer
                chip.save()
                return redirect('blog:chip_detail', pk=chip.pk)
            else:
                chip = chip_ex
                return redirect('blog:chip_detail_exist', pk=chip.pk)
    else:
        runForm = RunForm(prefix='run')
        waferForm = WaferForm(prefix='wafer')
        chipForm = ChipForm(prefix='chip')
        # waveguideFrom = WaveguideForm(prefix='waveguide')
    return render(request, 'blog/chip_edit.html', {'runForm': runForm, 'waferForm': waferForm,
                                                   'chipForm': chipForm})


@login_required(login_url='/accounts/signin/')
def chip_edit(request, pk):
    """
    Chip_edit function docstring.

    This function shows the form to modify a chip.

    @param request: HTML request page.

    @param pk: primary key of the chip to modify.

    @return: First time, this shows the form to edit the chip information. If the form is
    completed, return the details of this chip.

    @raise 404: chip does not exists.
    """
    chip = get_object_or_404(Chip, pk=pk)
    if request.method == "POST":
        form = ChipForm(data=request.POST, instance=chip)
        if form.is_valid():
            chip = form.save(commit=False)
            chip.save()
            return redirect('blog:chip_detail', pk=chip.pk)
    else:
        runForm = RunForm(instance=chip.run)
        waferForm = WaferForm(instance=chip.wafer)
        chipForm = ChipForm(instance=chip)
    return render(request, 'blog/chip_edit.html', {'runForm': runForm, 'waferForm': waferForm,
                                                   'chipForm': chipForm})


@login_required(login_url='/accounts/signin/')
def chip_remove(request, pk):
    """
    Chip_remove function docstring.

    This function removes a chip.

    @param request: HTML request page.

    @param pk: primary key of the chip to remove.

    @return: list of chips.

    @raise 404: chip does not exists.
    """
    chip = get_object_or_404(Chip, pk=pk)
    wafer_id = chip.wafer
    chip.delete()
    return redirect('blog:wafer_chip_list', pk=wafer_id)


@login_required(login_url='/accounts/signin/')
def chip_waveguide_new(run, wafer, chip):
    """
    Chip_waveguide_new function docstring.

    This function creates all waveguides of a chip. This function uses a forms to create the new
    waveguides (Waveguide form).

    @param run: primary key of the run.
    @param wafer: primary key of the wafer.
    @param chip: primary key of the chip.
    """
    waveguideName = Name_Waveguide.objects.all()
    # print(waveguideName)

    for waveguide in waveguideName:
        # print(waveguide.name)
        waveguideForm = WaveguideForm()
        newWaveguide = waveguideForm.save(commit=False)
        newWaveguide.run = run
        newWaveguide.wafer = wafer
        newWaveguide.chip = chip
        newWaveguide.waveguide = waveguide
        newWaveguide.name = waveguide.name
        # print(newWaveguide)
        newWaveguide.save()
