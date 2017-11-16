"""register.py."""

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from blog.models import Full_Name_Users
from blog.forms import SignUpForm


def home(request):
    """
    Home function docstring.

    This function shows the main page.

    @param request: HTML request page.

    @return: Main page.
    """
    return render(request, 'blog/home.html')


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
