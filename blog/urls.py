"""urls.py."""

from django.conf.urls import url
from . import views

urlpatterns = [
    # #################### HOME #################### #
    url(r'^$', views.home, name='home'),

    # #################### SIGN UP #################### #
    url(r'^accounts/signup/$', views.signup, name='signup'),

    # #################### ELEMENT #################### #
    url(r'^element/$', views.element_list, name='element_list'),
    url(r'^element/(?P<pk>[0-9]+)/$', views.element_detail, name='element_detail'),
    url(r'^element/new/$', views.element_new, name='element_new'),
    url(r'^element/(?P<pk>[0-9]+)/edit/$', views.element_edit, name='element_edit'),
    url(r'^element/(?P<pk>\d+)/remove/$', views.element_remove, name='element_remove'),

    # #################### COMPUTING #################### #
    url(r'^computing/$', views.computing_list, name='computing_list'),
    url(r'^computing/(?P<pk>[0-9]+)/$', views.computing_detail, name='computing_detail'),
    url(r'^computing/new/$', views.computing_new, name='computing_new'),
    url(r'^computing/(?P<pk>[0-9]+)/edit/$', views.computing_edit, name='computing_edit'),
    url(r'^computing/(?P<pk>\d+)/remove/$', views.computing_remove, name='computing_remove'),

    # #################### ELECTRONIC #################### #
    url(r'^electronic/$', views.electronic_list, name='electronic_list'),
    url(r'^electronic/(?P<pk>[0-9]+)/$', views.electronic_detail, name='electronic_detail'),
    url(r'^electronic/new/$', views.electronic_new, name='electronic_new'),
    url(r'^electronic/(?P<pk>[0-9]+)/edit/$', views.electronic_edit, name='electronic_edit'),
    url(r'^electronic/(?P<pk>\d+)/remove/$', views.electronic_remove, name='electronic_remove'),

    # #################### CHEMICAL ##################### #
    url(r'^chemical/$', views.chemical_list, name='chemical_list'),
    url(r'^chemical/(?P<pk>[0-9]+)/$', views.chemical_detail, name='chemical_detail'),
    url(r'^chemical/new/$', views.chemical_new, name='chemical_new'),
    url(r'^chemical/(?P<pk>[0-9]+)/edit/$', views.chemical_edit, name='chemical_edit'),
    url(r'^chemical/(?P<pk>\d+)/remove/$', views.chemical_remove, name='chemical_remove'),

    # #################### INSTRUMENTATION #################### #
    url(r'^instrumentation/$', views.instrumentation_list, name='instrumentation_list'),
    url(r'^instrumentation/(?P<pk>[0-9]+)/$', views.instrumentation_detail,
        name='instrumentation_detail'),
    url(r'^instrumentation/new/$', views.instrumentation_new, name='instrumentation_new'),
    url(r'^instrumentation/(?P<pk>[0-9]+)/edit/$', views.instrumentation_edit,
        name='instrumentation_edit'),
    url(r'^instrumentation/(?P<pk>\d+)/remove/$', views.instrumentation_remove,
        name='instrumentation_remove'),

    # #################### OTHERS #################### #
    url(r'^others/$', views.others_list, name='others_list'),
    url(r'^others/(?P<pk>[0-9]+)/$', views.others_detail, name='others_detail'),
    url(r'^others/new/$', views.others_new, name='others_new'),
    url(r'^others/(?P<pk>[0-9]+)/edit/$', views.others_edit, name='others_edit'),
    url(r'^others/(?P<pk>\d+)/remove/$', views.others_remove, name='others_remove'),

    # #################### ORDER #################### #
    url(r'^order/$', views.order_list, name='order_list'),
    url(r'^order/detail/(?P<pk>[0-9]+)/$', views.order_detail, name='order_detail'),
    url(r'^order/new/$', views.order_new, name='order_new'),
    url(r'^order/new/(?P<pk>[0-9]+)/$', views.order_new_next, name='order_new_next'),
    url(r'^order/(?P<pk>[0-9]+)/edit/$', views.order_edit, name='order_edit'),
    url(r'^order/(?P<pk>\d+)/remove/$', views.order_remove, name='order_remove'),

    # #################### RUN #################### #
    url(r'^run/$', views.run_list, name='run_list'),
    url(r'^run/(?P<pk>[0-9]+)/$', views.run_chip_list, name='run_chip_list'),

    # #################### CHIP #################### #
    url(r'^chip/$', views.chip_list, name='chip_list'),
    url(r'^chip/(?P<pk>[0-9]+)/$', views.chip_detail, name='chip_detail'),
    url(r'^chip/exist/(?P<pk>[0-9]+)/$', views.chip_detail_exist, name='chip_detail_exist'),
    url(r'^chip/new/$', views.chip_new, name='chip_new'),
    url(r'^chip/(?P<pk>[0-9]+)/edit/$', views.chip_edit, name='chip_edit'),
    url(r'^chip/(?P<pk>\d+)/remove/$', views.chip_remove, name='chip_remove'),

    # #################### WAVEGUIDE #################### #
    url(r'^waveguide/(?P<pk>[0-9]+)/$', views.waveguide_list, name='waveguide_list'),
    url(r'^waveguide/(?P<pk>[0-9]+)/detail/(?P<pk2>[0-9]+)/$', views.waveguide_detail,
        name='waveguide_detail'),
    url(r'^waveguide/(?P<pk>[0-9]+)/exist/(?P<pk2>[0-9]+)/$', views.waveguide_detail_exist,
        name='waveguide_detail_exist'),
    url(r'^waveguide/new/(?P<pk>[0-9]+)/$', views.waveguide_new, name='waveguide_new'),
    url(r'^waveguide/(?P<pk>[0-9]+)/edit/$', views.waveguide_edit, name='waveguide_edit'),
    url(r'^waveguide/(?P<pk>\d+)/remove/$', views.waveguide_remove, name='waveguide_remove'),
]
