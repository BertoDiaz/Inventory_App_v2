"""
mysite URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

"""

from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # url(r'^accounts/login/$', views.login, name='login'),
    # url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    # url(r'^accounts/password/reset/$', views.password_reset,
    #     {'template_name': 'registration/password_resetform.html'}, name='password_reset'),
    # url(r'^accounts/password/reset/done/$', views.password_reset_done,
    #     {'template_name': 'registration/password_resetdone.html'}, name='password_reset_done'),
    # url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #     views.password_reset_confirm, {'template_name': 'registration/password_resetconfirm.html'},
    #     name='password_reset_confirm'),
    # url(r'^accounts/password/done/$', views.password_reset_complete,
    #     {'template_name': 'registration/password_resetcomplete.html'}, name='password_reset_complete'),
    url(r'', include('blog.urls', namespace='blog')),
]
