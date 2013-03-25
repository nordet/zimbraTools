# -*- coding: utf-8 -*-
'''
Created on 23 mars 2013

@author: pascal
'''
from django.db import models
from django.utils.translation import ugettext_lazy as _

class ZimbraServerClass(models.Model):
  host = models.CharField(_(u"host of Zimbra server"), max_length=80)

  def __unicode__(self):
    return self.host
  
  class Meta:
    app_label = 'removeDoublons'
