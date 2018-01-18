"""
File name: waveguide.py

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
from blog.models import Run, Chip, Waveguide
from blog.forms import WaveguideForm


# def waveguide_list(request):
#
#     waveguides = Waveguide.objects.filter(
#        created_date__lte=timezone.now()).order_by('created_date')
#
#     return render(request, 'blog/waveguide_list.html', {'waveguides': waveguides})

@login_required
def waveguide_list(request, pk):
    """
    Waveguide_list function docstring.

    This function shows the list of waveguides of a chip that are stored in this web app.

    @param request: HTML request page.

    @param pk: primary key of the chip.

    @return: list of waveguides of a chip.
    """
    waveguides = Waveguide.objects.filter(chip=pk)
    chipBack = True
    waveguideBack = False

    return render(request, 'blog/waveguide_list.html', {'waveguides': waveguides, 'chip': pk,
                                                        'chipBack': chipBack,
                                                        'waveguideBack': waveguideBack})


# def waveguide_detail(request, pk, pk2):
@login_required
def waveguide_detail(request, pk):
    """
    Waveguide_detail function docstring.

    This function shows the information of a waveguide of a chip.

    @param request: HTML request page.

    @param pk: primary key of the chip.

    @param pk2: primary key of the waveguide.

    @return: one waveguide.

    @raise 404: waveguide does not exists.
    """
    waveguide = get_object_or_404(Waveguide, pk=pk)
    chipBack = False
    waveguideBack = True

    return render(request, 'blog/waveguide_detail.html', {'waveguide': waveguide,
                                                          'chipBack': chipBack,
                                                          'waveguideBack': waveguideBack})


@login_required
def waveguide_detail_exist(request, pk, pk2):
    """
    Waveguide_detail_exist function docstring.

    This function shows the information of a waveguide of a chip when a waveguide is created but
    this already exists.

    @param request: HTML request page.

    @param pk: primary key of the chip.

    @param pk2: primary key of the waveguide.

    @return: one waveguide.

    @raise 404: waveguide does not exists.
    """
    waveguide = get_object_or_404(Waveguide, pk=pk2)

    return render(request, 'blog/waveguide_detail_exist.html', {'waveguide': waveguide})


@login_required
def waveguide_new(request, pk):
    """
    Waveguide_new function docstring.

    This function shows the form to create a new waveguide of a chip. When the form is completed,
    this function search if the waveguide already exists.

    @param request: HTML request page.

    @param pk: primary key of the chip.

    @return: First time, this shows the form to a new waveguide to a chip already created. If the
    form is completed and waveguide does not exists, return the details of this new waveguide.

    @raise 404: chip does not exists.
    """
    if request.method == "POST":
        # runForm = RunForm(request.POST, prefix='run')
        # waferForm = WaferForm(request.POST, prefix='wafer')
        waveguideForm = WaveguideForm(request.POST, prefix='waveguide')
        # waveguideForm = WaveguideForm(request.POST, prefix='waveguide')
        # if runForm.is_valid():
        #     run = runForm.save(commit=False)
        #     run_ex = Run.objects.get(run=run.run)
        #     print(run)
        #     if not run_ex:
        #         # print(run_ex)
        #         run.save()
        #     else:
        #         run = run_ex
        # if waferForm.is_valid():
        #     wafer = waferForm.save(commit=False)
        #     wafer_ex = Wafer.objects.get(wafer=wafer.wafer, run=run)
        #     # print(wafer)
        #     if not wafer_ex:
        #         # print(wafer_ex)
        #         wafer.run = run
        #         wafer.save()
        #     else:
        #         wafer = wafer_ex
        if waveguideForm.is_valid():
            waveguide = waveguideForm.save(commit=False)
            # print(waveguide)
            chip = Chip.objects.get(pk=pk)
            # print(chip.wafer)
            waveguide_ex = Waveguide.objects.get(waveguide=waveguide.waveguide, chip=chip,
                                                 wafer=chip.wafer, run=chip.run)
            # print(waveguide)
            if not waveguide_ex:
                # print(waveguide_ex)
                waveguide.run = chip.run
                waveguide.wafer = chip.wafer
                waveguide.chip = chip
                waveguide.name = waveguide.waveguide.name
                waveguide.save()
                return redirect('blog:waveguide_detail', pk=chip.pk, pk2=waveguide.pk)
            else:
                waveguide = waveguide_ex
                print(waveguide.pk)
                return redirect('blog:waveguide_detail_exist', pk=chip.pk, pk2=waveguide.pk)
    else:
        # runForm = RunForm(prefix='run')
        # waferForm = WaferForm(prefix='wafer')
        chip = get_object_or_404(Chip, pk=pk)
        waveguideForm = WaveguideForm(prefix='waveguide')
        # waveguideFrom = WaveguideForm(prefix='waveguide')
    return render(request, 'blog/waveguide_edit.html', {'waveguideForm': waveguideForm,
                                                        'chip': chip})


@login_required
def waveguide_edit(request, pk):
    """
    Waveguide_edit function docstring.

    This function shows the form to modify a waveguide.

    @param request: HTML request page.

    @param pk: primary key of the waveguide to modify.

    @return: First time, this shows the form to edit the waveguide information. If the form is
    completed, return the details of this waveguide.

    @raise 404: waveguide does not exists.
    """
    waveguide_data = Waveguide.objects.get(pk=pk)
    if request.method == "POST":
        form = WaveguideForm(data=request.POST)
        waveguide_data = Waveguide.objects.get(pk=pk)
        if form.is_valid():
            waveguide_data.amplitude = form.cleaned_data['amplitude']
            waveguide_data.offset = form.cleaned_data['offset']
            waveguide_data.frecuency = form.cleaned_data['frecuency']
            waveguide_data.i_up = form.cleaned_data['i_up']
            waveguide_data.i_down = form.cleaned_data['i_down']
            waveguide_data.slope = form.cleaned_data['slope']
            waveguide_data.visibility = form.cleaned_data['visibility']
            waveguide_data.noise = form.cleaned_data['noise']
            waveguide_data.lod = form.cleaned_data['lod']
            waveguide_data.save()
            return redirect('blog:waveguide_detail', pk=waveguide_data.pk)
    else:
        form = WaveguideForm(instance=waveguide_data)
    return render(request, 'blog/waveguide_edit.html', {'form': form})


@login_required
def waveguide_remove(request, pk):
    """
    Waveguide_remove function docstring.

    This function removes a waveguide.

    @param request: HTML request page.

    @param pk: primary key of the waveguide to remove.

    @return: list of waveguides.

    @raise 404: waveguide does not exists.
    """
    waveguide = get_object_or_404(Run, pk=pk)
    waveguide.delete()
    return redirect('blog:waveguide_list')
