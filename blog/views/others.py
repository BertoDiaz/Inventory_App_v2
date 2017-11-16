"""others.py."""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from blog.models import Others
from blog.forms import OthersForm


def others_list(request):
    """
    Others_list function docstring.

    This function shows the list of components whithout type that are stored in this web app and
    they are ordered by creation date.

    @param request: HTML request page.

    @return: list of components whithout type.
    """
    otherss = Others.objects.filter(
        created_date__lte=timezone.now()).order_by('created_date').reverse()

    return render(request, 'blog/others_list.html', {'otherss': otherss})


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
