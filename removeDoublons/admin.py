# -*- coding: utf-8 -*-
'''
Created on 23 mars 2013

@author: pascal
'''
from django.contrib import admin
from removeDoublons.models import ZimbraServerClass, LdapServerClass

admin.site.register(ZimbraServerClass)
admin.site.register(LdapServerClass)
