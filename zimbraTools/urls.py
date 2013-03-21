# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'clearCalendarZimbra.views.home', name='home'),
    # url(r'^clearCalendarZimbra/', include('clearCalendarZimbra.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # If you are using ^/profile/ ... for anything else (e.g. /profile/<username>),
    # remember that this must go AFTER the two lines following, otherwise you will get
    # errors (it will try to look up 'password' as a user.
    (r'^profile/password/$', 'django_ldapbackend.views.password_change'),
    (r'^profile/password/changed/$', 'django.contrib.auth.views.password_change_done'),
    url(r'^$', 'removeDoublons.views.home', name='home'),
    url(r'^select_compte', 'removeDoublons.views.select_compte', name='select_compte'),
    url(r'^fileToClean', 'removeDoublons.views.fileToClean', name='fileToClean'),
    url(r'^fileCleanAgenda', 'removeDoublons.views.fileCleanAgenda', name='fileCleanAgenda'),
    url(r'^(?P<compte>.+)/calendar/', 'removeDoublons.views.calendarToClean', name='calendarToClean'),
    url(r'^login_interne', 'removeDoublons.views.login_interne', name='login_interne'),
    url(r'^message', 'removeDoublons.views.message', name='message'),
    # (r'^$' , login_required(direct_to_template, redirect_field_name='', {'template':'registration/login.html' }),
    (r'^login$', 'django.contrib.auth.views.login'),
    url(r'^logout_view$', 'removeDoublons.views.logout_view', name='logout_view'),
    # (r'^join$', 'engine.views.join'),
    # (r'^dashboard$', 'engine.views.dashboard'),
)
