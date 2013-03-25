# -*- coding: utf-8 -*-
# Create your forms here.
from django import forms
from django.core.context_processors import csrf
from removeDoublons.models.ComptesZimbra import ComptesZimbra
from removeDoublons.models.CalendriersCompteZimbra import CalendriersCompteZimbra
from tools.list2tuple import list2tuple
from django.contrib.sessions.models import Session
from django.http import QueryDict
from removeDoublons.models.ZimbraServerClass import ZimbraServerClass

class UploadFileForm(forms.Form):
  file = forms.FileField()

class SelectCompteForm(forms.Form):
  def __init__(self, zimbraServer=None, *args, **kwargs):
    super(SelectCompteForm, self).__init__(*args, **kwargs)
    if not isinstance(zimbraServer, QueryDict):
      print "SelectCompteForm : QueryDict = ", QueryDict
      print "SelectCompteForm : zimbraServer = ", zimbraServer
      comptes = ComptesZimbra(zimbraServer)
      tupleListe = list2tuple(comptes.liste)
      print "=====SelectCompteForm : tupleListe = ", tupleListe
      self.fields['compte'] = forms.ChoiceField(choices=tupleListe)

class SelectCalendarForm(forms.Form):
  def __init__(self, compte=None, zimbraServer=None, *args, **kwargs):
    super(SelectCalendarForm, self).__init__(*args, **kwargs)
    if not isinstance(compte, QueryDict) :
      calendriers = CalendriersCompteZimbra(compte, zimbraServer)
      tupleListe = list2tuple(calendriers.liste)
      self.data['cpte'] = compte
      self.fields['calendrier'] = forms.ChoiceField(choices=tupleListe)

class LoginForm(forms.Form):
  userName = forms.CharField()
  userPassword = forms.CharField(widget=forms.PasswordInput())
  host = forms.ModelChoiceField(ZimbraServerClass.objects.all())
