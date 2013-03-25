# -*- coding: utf-8 -*-
'''
Created on 23 mars 2013

@author: pascal
'''
from django.db import models
from django.utils.translation import ugettext_lazy as _
from ZimbraServerClass import ZimbraServerClass

class LdapServerClass(models.Model):
  host = models.CharField(_(u"host of Zimbra server"), max_length=80)
  port = models.IntegerField(_(u"port of Zimbra server"))
  user = models.CharField(_(u"user for Zimbra server"), max_length=80)
  password = models.CharField(_(u"password for Zimbra server"), max_length=20)
  userdn = models.CharField(_(u"user dn for Zimbra server"), max_length=100)
  zimbraServer = models.ForeignKey(ZimbraServerClass)

  def __unicode__(self):
    return self.host
  
  class Meta:
    app_label = 'removeDoublons'
