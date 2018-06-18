"""
File name: messages.py.

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
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.encoders import encode_base64
import smtplib
from blog.views.search import get_query
from blog.models import Messages, Full_Name_Users
from blog.forms import MessagesForm, NotifyToForm


@login_required
def messages_list(request):
    """
    Messages_list function docstring.

    This function shows the list of messages that are stored in this web app and they are
    ordered by creation date.

    @param request: HTML request page.

    @return: list of messages.
    """
    if request.user.is_staff:
        messages_list = Messages.objects.all().order_by('created_date').reverse()

        findSomething = messages_list.exists()
        is_search = False

        # Show 25 contacts per page
        paginator = Paginator(messages_list, 25)

        page = request.GET.get('page')
        try:
            messagesInfo = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            messagesInfo = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            messagesInfo = paginator.page(paginator.num_pages)

        return render(request, 'blog/messages_list.html', {'messagesInfo': messagesInfo,
                                                           'findSomething': findSomething,
                                                           'is_search': is_search})
    else:
        messages.warning(request, 'Ups!! You do not have privileges.')

    return render(request, 'blog/messages_list.html')


@login_required
def messages_search(request):
    """
    Messages_search function docstring.

    This function search the messages that are stored in this web app and they are
    ordered by creation date.

    @param request: HTML request page.

    @return: list of messages.
    """
    query_string = ''
    found_entries = None
    exists = False
    if ('searchfield' in request.GET) and request.GET['searchfield'].strip():
        query_string = request.GET['searchfield']
        try:
            entry_query = get_query(query_string, ['username', 'first_name', 'last_name'])
            author = User.objects.get(entry_query)
            exists = True
        except ObjectDoesNotExist:
            entry_query = get_query(query_string, ['messageText'])
            message_list = Messages.objects.filter(entry_query).order_by('created_date').reverse()
            exists = False

    if exists:
        message_list = Messages.objects.filter(author=author).order_by('created_date').reverse()

    findSomethingSearch = message_list.exists()
    is_search = True

    # Show 25 contacts per page
    paginator = Paginator(message_list, 25)

    page = request.GET.get('page')
    try:
        messagesInfo = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        messagesInfo = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        messagesInfo = paginator.page(paginator.num_pages)

    return render(request, 'blog/messages_list.html', {'messagesInfo': messagesInfo,
                                                       'findSomethingSearch': findSomethingSearch,
                                                       'is_search': is_search})


@login_required
def messages_detail(request, pk):
    """
    Messages_detail function docstring.

    This function shows the information of a message.

    @param request: HTML request page.

    @param pk: primary key of the message.

    @return: one message.

    @raise 404: message does not exists.
    """
    messageInfo = get_object_or_404(Messages, pk=pk)

    backList = True

    return render(request, 'blog/messages_detail.html', {'messageInfo': messageInfo,
                                                         'backList': backList})


@login_required
def messages_new(request):
    """
    Messages_new function docstring.

    This function shows the form to create a new message.

    @param request: HTML request page.

    @return: First time, this shows the form to a new message. If the form is completed, return the
    details of this new message.
    """
    if request.method == "POST":
        form = MessagesForm(request.POST, prefix="messages")
        notify_form = NotifyToForm(request.POST, prefix="notify")
        # print(notify_form)
        # print(request.POST.get("notifyStaff"))
        if form.is_valid() and notify_form.is_valid():
            messageInfo = form.save(commit=False)
            messageInfo.author = request.user
            messageInfo.show = True
            messages_all = Messages.objects.all()

            duplicates = False

            for data in messages_all:
                if (data.messageText == messageInfo.messageText) and (data.pk != messageInfo.pk):
                    if data.show:
                        duplicates = True
                        message_ex = data

            if not duplicates:
                messages.success(request, 'You have added your message successfully.')

                username_author = User.objects.get(username=messageInfo.author)

                if notify_form.cleaned_data['notifyStaff']:
                    fromaddr = "heriberto.diazluis@gmail.com"
                    toaddrs = "heriberto.diaz@icn2.cat"
                    subject = 'New Comment'

                elif notify_form.cleaned_data['notifyGroup']:
                    fromaddr = "heriberto.diazluis@gmail.com"
                    toaddrs = "grupotestdjango@googlegroups.com"
                    subject = 'New Comment'

                message_1 = "<p>Hello everybody,</p><p>There is a new comment in the Web app of " + username_author.first_name + ":</p>"
                message_2 = "<p style='padding-left: 20px;'><i>'" + messageInfo.messageText + "'</i></p><p>Best regards,</p><p>" + username_author.first_name + "</p>"
                message = message_1 + message_2

                msg = MIMEMultipart('related')
                msg['From'] = fromaddr
                msg['To'] = toaddrs
                msg['Subject'] = subject

                # Content-type:text/html
                message = MIMEText(message, 'html')
                msg.attach(message)

                try:
                    # ENVIAR
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    # protocolo de cifrado de datos utilizado por gmail
                    server.starttls()
                    # Credenciales
                    # Añadir nombre de usuario y contraseña con el siguiente comando
                    # server.login(username, password)
                    server.login("heriberto.diazluis@gmail.com", 'heriberto_20')
                    server.set_debuglevel(1)
                    server.sendmail(fromaddr, toaddrs, msg.as_string())
                    server.quit()

                    # messages.success(request, 'The group has been notified successfully.')

                except smtplib.SMTPException:
                    messages.error(request,
                                   'There was a error with username or password. You have to notify this error to the '
                                   'admin.')

                # return redirect('blog:order_detail', pk=pk)

                messageInfo.save()
            else:
                messages.warning(request,
                                 'Ups!! A message with this text already exists. If you want to do any change, please '
                                 'edit it.')
                messageInfo = message_ex

            return redirect('blog:messages_detail', pk=messageInfo.pk)
    else:
        form = MessagesForm(prefix="messages")
        notify_form = NotifyToForm(prefix="notify")
    return render(request, 'blog/messages_new.html', {'form': form, 'notify': notify_form})


@login_required
def messages_edit(request, pk):
    """
    Messages_edit function docstring.

    This function shows the form to modify a message.

    @param request: HTML request page.

    @param pk: primary key of the message to modify.

    @return: First time, this shows the form to edit the message text. If the form is
    completed, return the details of this message.

    @raise 404: message does not exists.
    """
    messageInfo = get_object_or_404(Messages, pk=pk)

    if request.method == "POST":
        message_form = MessagesForm(data=request.POST, instance=messageInfo)
        if message_form.is_valid():
            messageInfo = message_form.save(commit=False)

            userEdit = User.objects.get(username=request.user.username)

            if not userEdit.is_staff:
                messageInfo.author = request.user
                messageInfo.show = True

            messages_all = Messages.objects.all()

            duplicates = False

            for data in messages_all:
                if (data.messageText == messageInfo.messageText) and (data.pk != messageInfo.pk):
                    if data.show:
                        duplicates = True

            if not duplicates:
                messages.success(request, 'You have updated your message.')
                messageInfo.save()
                return redirect('blog:messages_detail', pk=messageInfo.pk)
            else:
                messages.warning(request, 'Already exists a message with this text.')
                return redirect('blog:messages_edit', pk=messageInfo.pk)

    else:
        form = MessagesForm(instance=messageInfo)
    return render(request, 'blog/messages_edit.html', {'form': form})


@login_required
def messages_remove(request, pk):
    """
    Messages_remove function docstring.

    This function removes a message.

    @param request: HTML request page.

    @param pk: primary key of the message to remove.

    @return: list of messages.

    @raise 404: message does not exists.
    """
    messageInfo = get_object_or_404(Messages, pk=pk)
    messageInfo.delete()
    return redirect('blog:messages_list')
