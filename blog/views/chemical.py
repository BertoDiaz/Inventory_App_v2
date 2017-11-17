"""chemical.py."""

from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from blog.models import Chemical, Type_Chemical, State
from blog.forms import ChemicalForm


def chemical_list_type_chemical(request):
    """
    Chemical_list_type_chemical function docstring.

    This function shows the list of type of chemicals that are stored in this web app and they are
    ordered by creation date.

    @param request: HTML request page.

    @return: list of type of chemicals.
    """
    states = State.objects.all()
    chemicals = Type_Chemical.objects.all()

    return render(request, 'blog/chemical_list_type_chemical.html', {'states': states,
                                                                     'chemicals': chemicals})


def chemical_list(request, pk):
    """
    Chemical_list function docstring.

    This function shows the list of chemicals that are stored in this web app and they are
    ordered by creation date.

    @param request: HTML request page.
    @param pk: primary key of chemical type.

    @return: list of chemicals.
    """
    type_chemical = Type_Chemical.objects.get(pk=pk)
    chemical_list = Chemical.objects.filter(type_chemical=type_chemical).order_by('name')

    # Show 25 contacts per page
    paginator = Paginator(chemical_list, 10)

    page = request.GET.get('page')
    try:
        chemicals = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        chemicals = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        chemicals = paginator.page(paginator.num_pages)

    chemicalsBack = True
    type_chemicalBack = False

    return render(request, 'blog/chemical_list.html', {'chemicals': chemicals,
                                                       'chemicalsBack': chemicalsBack,
                                                       'type_chemicalBack': type_chemicalBack})


def chemical_detail(request, pk):
    """
    Chemical_detail function docstring.

    This function shows the information of a chemical.

    @param request: HTML request page.

    @param pk: primary key of the chemical.

    @return: one chemical.

    @raise 404: chemical does not exists.
    """
    chemical = get_object_or_404(Chemical, pk=pk)
    chemicalsBack = False
    type_chemicalBack = True

    return render(request, 'blog/chemical_detail.html', {'chemical': chemical,
                                                         'chemicalsBack': chemicalsBack,
                                                         'type_chemicalBack': type_chemicalBack})


@login_required
def chemical_new(request):
    """
    Chemical_new function docstring.

    This function shows the form to create a new chemical.

    @param request: HTML request page.

    @return: First time, this shows the form to a new chemical. If the form is completed, return
    the details of this new chemical.
    """
    if request.method == "POST":
        form = ChemicalForm(request.POST)
        if form.is_valid():
            chemical = form.save(commit=False)
            chemical.save()
            return redirect('blog:chemical_detail', pk=chemical.pk)
    else:
        form = ChemicalForm()
    return render(request, 'blog/chemical_new.html', {'form': form})


@login_required
def chemical_edit(request, pk):
    """
    Chemical_edit function docstring.

    This function shows the form to modify a chemical.

    @param request: HTML request page.

    @param pk: primary key of the chemical to modify.

    @return: First time, this shows the form to edit the chemical information. If the form is
    completed, return the details of this chemical.

    @raise 404: chemical does not exists.
    """
    chemical = get_object_or_404(Chemical, pk=pk)
    if request.method == "POST":
        form = ChemicalForm(data=request.POST, instance=chemical)
        if form.is_valid():
            chemical = form.save(commit=False)
            chemical_all = Chemical.objects.all()

            duplicates = False

            for data in chemical_all:
                if data.name == chemical.name and data.pk != chemical.pk:
                    duplicates = True

            if not duplicates:
                messages.success(request, 'You have updated your chemical.')
                chemical.save()
                return redirect('blog:chemical_detail', pk=chemical.pk)
            else:
                messages.warning(request, 'Already exists an chemical with this name.')
                return redirect('blog:chemical_edit', pk=chemical.pk)

    else:
        form = ChemicalForm(instance=chemical)
    return render(request, 'blog/chemical_edit.html', {'form': form})


@login_required
def chemical_remove(request, pk):
    """
    Chemical_remove function docstring.

    This function removes a chemical.

    @param request: HTML request page.

    @param pk: primary key of the chemical to remove.

    @return: list of chemicals.

    @raise 404: chemical does not exists.
    """
    chemical = get_object_or_404(Chemical, pk=pk)
    chemical.delete()
    return redirect('blog:chemical_list')
