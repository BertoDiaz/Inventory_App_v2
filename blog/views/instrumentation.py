"""instrumentation.py."""

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import Instrumentation, Type_Instrumentation
from blog.forms import InstrumentationForm


def instrumentation_list_type(request):
    """
    Instrumentation_list_type function docstring.

    This function shows the list of instrument types that are stored in this web app and they are
    ordered by creation date.

    @param request: HTML request page.

    @return: list of instrument types.
    """
    instrumentations = Type_Instrumentation.objects.all()

    return render(request, 'blog/instrumentation_list_type.html',
                  {'instrumentations': instrumentations})


def instrumentation_list(request, pk):
    """
    Instrumentation_list function docstring.

    This function shows the list of instruments that are stored in this web app and they are
    ordered by creation date.

    @param request: HTML request page.
    @param pk: primary key of instrument types..

    @return: list of instrument types.
    """
    type_instrumentation = Type_Instrumentation.objects.get(pk=pk)
    instrumentations = Instrumentation.objects.filter(
        type_instrumentation=type_instrumentation).order_by('characteristics')
    instrumentBack = True
    type_instrumBack = False

    return render(request, 'blog/instrumentation_list.html', {'instrumentations': instrumentations,
                                                              'instrumentBack': instrumentBack,
                                                              'type_instrumBack': type_instrumBack})


def instrumentation_detail(request, pk):
    """
    Instrumentation_detail function docstring.

    This function shows the information of a instrument.

    @param request: HTML request page.

    @param pk: primary key of the instrument.

    @return: one instrument.

    @raise 404: instrument does not exists.
    """
    instrumentation = get_object_or_404(Instrumentation, pk=pk)
    instrumentBack = False
    type_instrumBack = True

    return render(request, 'blog/instrumentation_detail.html', {'instrumentation': instrumentation,
                                                                'instrumentBack': instrumentBack,
                                                                'type_instrumBack': type_instrumBack
                                                                })


@login_required
def instrumentation_new(request):
    """
    Instrumentation_new function docstring.

    This function shows the form to create a new instrument.

    @param request: HTML request page.

    @return: First time, this shows the form to a new instrument. If the form is completed, return
    the details of this new instrument.
    """
    if request.method == "POST":
        form = InstrumentationForm(request.POST)
        if form.is_valid():
            instrumentation = form.save(commit=False)
            instrumentation.save()
            return redirect('blog:instrumentation_detail', pk=instrumentation.pk)
    else:
        form = InstrumentationForm()
    return render(request, 'blog/instrumentation_new.html', {'form': form})


@login_required
def instrumentation_edit(request, pk):
    """
    Instrumentation_edit function docstring.

    This function shows the form to modify a instrument.

    @param request: HTML request page.

    @param pk: primary key of the instrument to modify.

    @return: First time, this shows the form to edit the instrument information. If the form is
    completed, return the details of this instrument.

    @raise 404: instrument does not exists.
    """
    instrumentation = get_object_or_404(Instrumentation, pk=pk)
    if request.method == "POST":
        form = InstrumentationForm(data=request.POST, instance=instrumentation)
        if form.is_valid():
            instrumentation = form.save(commit=False)
            instrumentation_all = Instrumentation.objects.all()

            duplicates = False

            for data in instrumentation_all:
                if data.characteristics == instrumentation.characteristics:
                    if data.pk != instrumentation.pk:
                        duplicates = True

            if not duplicates:
                messages.success(request, 'You have updated your instrumentation.')
                instrumentation.save()
                return redirect('blog:instrumentation_detail', pk=instrumentation.pk)
            else:
                messages.warning(request, 'Already exists an instrumentation with this name.')
                return redirect('blog:instrumentation_edit', pk=instrumentation.pk)

    else:
        form = InstrumentationForm(instance=instrumentation)
    return render(request, 'blog/instrumentation_edit.html', {'form': form})


@login_required
def instrumentation_remove(request, pk):
    """
    Instrumentation_remove function docstring.

    This function removes a instrument.

    @param request: HTML request page.

    @param pk: primary key of the instrument to remove.

    @return: list of instruments.

    @raise 404: instrument does not exists.
    """
    instrumentation = get_object_or_404(Instrumentation, pk=pk)
    instrumentation.delete()
    return redirect('blog:instrumentation_list')
