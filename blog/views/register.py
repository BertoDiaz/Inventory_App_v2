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
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from blog.models import Full_Name_Users, Messages
from blog.forms import SignUpForm


import ldap


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
        form = SignUpForm(request.POST, prefix="register")
        # fullName_form = FullNameForm(request.POST, prefix="fullName")
        if form.is_valid():
            form.save()
            firstname = form.cleaned_data.get('first_name')
            lastname = form.cleaned_data.get('last_name')
            nameFull = firstname + ' ' + lastname
            fullName = Full_Name_Users()
            fullName.name = nameFull
            # fullName.email_gmail = fullName_form.cleaned_data.get('email_gmail')
            fullName.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('blog:home')
    else:
        form = SignUpForm(prefix="register")
    return render(request, 'registration/signup.html', {'form': form})


def signin(request):
    """
    Sign in function docstring.

    This function carries out the login of user.

    @param request: HTML request page.

    @return: First time, return to sign in page. If the login is right, return to home
    page with your username.
    """
    if request.method == 'POST':

        username = '%s@icn2.net' % request.POST.get('Username')

        try:
            connection = ldap.initialize('ldap://icn2.net')
            connection.set_option(ldap.OPT_REFERRALS, 0)

            connection.simple_bind_s(username, request.POST.get('Password'))

            base_dn = 'DC=icn2,DC=net'
            ldap_filter = 'userPrincipalName=%s' % username

            ldap_client = connection.search_s(base_dn, ldap.SCOPE_SUBTREE, ldap_filter)

            firstName = ldap_client[0][1]['givenName'][0].decode('utf-8')
            lastName = ldap_client[0][1]['sn'][0].decode('utf-8')
            mail = ldap_client[0][1]['mail'][0].decode('utf-8')
            # fullName = ldap_client[0][1]['name'][0].decode('utf-8')

        except ldap.INVALID_CREDENTIALS:
            messages.error(request, 'Username or Password incorrect.')

            return render(request, 'registration/signin.html')

        except ldap.SERVER_DOWN:
            messages.error(request, 'Server is not available now, try again later.')

            return render(request, 'registration/signin.html')

        try:
            user = User.objects.get(username=request.POST.get('Username'))

        except User.DoesNotExist:
            user = User(username=request.POST.get('Username'), password=request.POST.get('Password'),
                        first_name=firstName, last_name=lastName, email=mail)
            user.is_active = True

        if not user.first_name:
            user.first_name = firstName

        if not user.last_name:
            user.last_name = lastName

        user.save()

        userAuthenticate = authenticate(username=request.POST.get('Username'), password=request.POST.get('Password'))

        if userAuthenticate is not None:
            login(request, userAuthenticate)

            return render(request, 'blog/home.html')

        else:
            user.set_password(request.POST.get('Password'))

            user.save()

            userAuthenticate = authenticate(username=request.POST.get('Username'),
                                            password=request.POST.get('Password'))

            login(request, userAuthenticate)

            return render(request, 'blog/home.html')

    else:
        return render(request, 'registration/signin.html')


def signout(request):
    """
    Sign out function docstring.

    This function carry out the logout.

    @param request: HTML request page.

    @return: Home page.
    """
    logout(request)

    return redirect('blog:home')
