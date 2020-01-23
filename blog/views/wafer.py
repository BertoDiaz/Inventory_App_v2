"""
File name: wafer.py.

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
from blog.models import Run, Wafer, Chip, Name_Waveguide
from blog.forms import RunForm, WaferForm, ChipForm, WaveguideForm


@login_required(login_url='/accounts/signin/')
def wafer_list(request, pk):
    """
    wafer_list function docstring.

    This function shows the list of wafers that are stored in this web app and they are ordered by
    creation date.

    @param request: HTML request page.

    @return: list of wafers.
    """
    wafers = Wafer.objects.filter(run=pk).order_by('created_date').reverse()

    return render(request, 'blog/wafer_list.html', {'wafers': wafers})


@login_required(login_url='/accounts/signin/')
def wafer_edit(request, pk):
    """
    Wafer_edit function docstring.

    This function shows the form to modify a wafer.

    @param request: HTML request page.

    @param pk: primary key of the wafer to modify.

    @return: First time, this shows the form to edit the wafer information. If the form is
    completed, return the wafer list.

    @raise 404: wafer does not exists.
    """
    wafer = get_object_or_404(Wafer, pk=pk)
    # wafer = Wafer.objects.filter(pk=pk)
    if request.method == "POST":
        form = WaferForm(data=request.POST, instance=wafer)
        if form.is_valid():
            wafer = form.save(commit=False)
            wafer_all = Wafer.objects.all()

            duplicates = False

            for data in wafer_all:
                if data.wafer == wafer.wafer and data.pk != wafer.pk:
                    duplicates = True
                    wafer_ex = data

            if not duplicates:
                # messages.success(request, 'You have added your chemical successfully.')
                wafer.name_wafer = str(wafer.wafer)
                wafer.comments = wafer.comments
                wafer.save()
            else:
                # messages.warning(request,
                #                  'Ups!! A chemical with this reference already exists. If you want to add a new '
                #                  'bottle to the stock, please edit it.')
                wafer = wafer_ex

            return redirect('blog:wafer_list', pk=wafer.run.pk)
    else:
        waferForm = WaferForm(instance=wafer)
    return render(request, 'blog/wafer_edit.html', {'waferForm': waferForm})


def wafer_chip_new(run, wafer):
    """
    Wafer_chip_new function docstring.

    This function creates all chips of a wafer. This function uses a forms to create the new
    chips (Chip form).

    @param run: primary key of the run.
    @param wafer: primary key of the wafer.
    """
    chipsName = ['CHIP1', 'CHIP2', 'CHIP3', 'CHIP4', 'CHIP5']
    chipsGName = ['CHIPG1', 'CHIPG2', 'CHIPG3', 'CHIPG4', 'CHIPG5']
    chipsPName = ['CHIP6P', 'CHIPG6P']

    for chipName in chipsName:
        chipForm = ChipForm()
        newChip = chipForm.save(commit=False)
        newChip.run = run
        newChip.wafer = wafer
        newChip.chip = chipName
        # print(newChip)
        newChip.save()
        chip_waveguide_new(run, wafer, newChip)

    for chipGName in chipsGName:
        chipForm = ChipForm()
        newChip = chipForm.save(commit=False)
        newChip.run = run
        newChip.wafer = wafer
        newChip.chip = chipGName
        # print(newChip)
        newChip.save()
        chip_waveguide_new(run, wafer, newChip)

    for chipPName in chipsPName:
        chipForm = ChipForm()
        newChip = chipForm.save(commit=False)
        newChip.run = run
        newChip.wafer = wafer
        newChip.chip = chipPName
        # print(newChip)
        newChip.save()
        chip_waveguide_new(run, wafer, newChip)


@login_required(login_url='/accounts/signin/')
def wafer_new(request):
    """
    wafer_new function docstring.

    This function shows the form to create a new wafer. This function uses 2 forms to create a new
    wafer (Run form and Wafer form), moreover, when the form is completed, this function
    search if the run or wafer already exists.

    @param request: HTML request page.

    @return: First time, this shows the form to a new wafer. If the form is completed and the run or
    wafer does not exists, return the list of chips of this new wafer.
    """
    if request.method == "POST":
        runForm = RunForm(request.POST, prefix='run')
        waferForm = WaferForm(request.POST, prefix='wafer')
        if runForm.is_valid():
            run = runForm.save(commit=False)
            # run_ex = Run.objects.get(run=run.run)
            run_ex = Run.objects.filter(run=run.run).exists()

            if not run_ex:
                run.save()
            else:
                # run = run_ex
                run = Run.objects.get(run=run.run)
        if waferForm.is_valid():
            wafer = waferForm.save(commit=False)
            # wafer_ex = Wafer.objects.get(wafer=wafer.wafer, run=run)
            wafer_ex = Wafer.objects.filter(name_wafer=wafer.name_wafer, run=run).exists()

            if not wafer_ex:
                wafer.run = run
                wafer.name_wafer = str(wafer.wafer)
                wafer.save()
                wafer_chip_new(run, wafer)
                return redirect('blog:wafer_chip_list', pk=wafer.pk)
            else:
                # wafer = wafer_ex
                wafer = Wafer.objects.get(wafer=wafer.wafer, run=run)
                return redirect('blog:wafer_detail_exist', pk=wafer.pk)
    else:
        runForm = RunForm(prefix='run')
        waferForm = WaferForm(prefix='wafer')
    return render(request, 'blog/wafer_edit.html', {'runForm': runForm, 'waferForm': waferForm})


@login_required(login_url='/accounts/signin/')
def wafer_chip_list(request, pk):
    """
    Wafer_chip_list function docstring.

    This function shows the list of chips of a wafer that are stored in this web app.

    @param request: HTML request page.

    @param pk: primary key of the wafer.

    @return: list of chips.
    """
    # chips = Chip.objects.filter(run=pk)
    chips = Chip.objects.filter(wafer=pk)
    run = Wafer.objects.get(pk=pk)
    # print(run.run.pk)
    runback = True
    waferback = False

    return render(request, 'blog/chip_list.html', {'chips': chips, 'runPK': run.run.pk,
                                                   'runback': runback, 'waferback': waferback})


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

    for waveguide in waveguideName:
        waveguideForm = WaveguideForm()
        newWaveguide = waveguideForm.save(commit=False)
        newWaveguide.run = run
        newWaveguide.wafer = wafer
        newWaveguide.chip = chip
        newWaveguide.waveguide = waveguide
        newWaveguide.name = waveguide.name
        newWaveguide.save()
