"""
File name: register.py.

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

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Full_Name_Users, Messages
from blog.forms import SignUpForm


def home(request):
    """
    Home function docstring.

    This function shows the main page.

    @param request: HTML request page.

    @return: Main page.
    """
    messages_list = Messages.objects.filter(show=True).order_by('created_date').reverse()

    # Show 25 contacts per page
    paginator = Paginator(messages_list, 8)

    page = request.GET.get('page')
    try:
        messagesInfo = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        messagesInfo = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        messagesInfo = paginator.page(paginator.num_pages)

    return render(request, 'blog/home.html', {'messagesInfo': messagesInfo})


def signup(request):
    """
    Signup function docstring.

    This function carries out the registration of a new user.

    @param request: HTML request page.

    @return: First time, return to sign up page. If the sign up form is completed, return to home
    page with your username.
    """
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')
            nameFull = firstname + ' ' + lastname
            fullName = Full_Name_Users()
            fullName.name = nameFull
            fullName.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('blog:home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
