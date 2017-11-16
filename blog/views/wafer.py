"""wafer.py."""

from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
from blog.models import Run, Wafer, Chip, Name_Waveguide
from blog.forms import RunForm, WaferForm, ChipForm, WaveguideForm


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


@login_required
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
            # print("Run: " + str(run_ex))
            if not run_ex:
                # print(run_ex)
                run.save()
            else:
                # run = run_ex
                run = Run.objects.get(run=run.run)
        if waferForm.is_valid():
            wafer = waferForm.save(commit=False)
            # wafer_ex = Wafer.objects.get(wafer=wafer.wafer, run=run)
            wafer_ex = Wafer.objects.filter(wafer=wafer.wafer, run=run).exists()
            # print("Wafer: " + str(wafer_ex))
            if not wafer_ex:
                # print(wafer_ex)
                wafer.run = run
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


def wafer_chip_new(run, wafer):
    """
    Wafer_chip_new function docstring.

    This function creates all chips of a wafer. This function uses a forms to create the new
    chips (Chip form).

    @param run: primary key of the run.
    @param wafer: primary key of the wafer.
    """
    chipName = ['CHIP1', 'CHIP2', 'CHIP3', 'CHIP4', 'CHIP5']
    chipGName = ['CHIPG1', 'CHIPG2', 'CHIPG3', 'CHIPG4', 'CHIPG5']
    chipPName = ['CHIP6P', 'CHIPG6P']

    for chip in chipName:
        chipForm = ChipForm()
        newChip = chipForm.save(commit=False)
        newChip.run = run
        newChip.wafer = wafer
        newChip.chip = chip
        # print(newChip)
        newChip.save()
        chip_waveguide_new(run, wafer, newChip)

    for chip in chipGName:
        chipForm = ChipForm()
        newChip = chipForm.save(commit=False)
        newChip.run = run
        newChip.wafer = wafer
        newChip.chip = chip
        # print(newChip)
        newChip.save()
        chip_waveguide_new(run, wafer, newChip)

    for chip in chipPName:
        chipForm = ChipForm()
        newChip = chipForm.save(commit=False)
        newChip.run = run
        newChip.wafer = wafer
        newChip.chip = chip
        # print(newChip)
        newChip.save()
        chip_waveguide_new(run, wafer, newChip)


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
