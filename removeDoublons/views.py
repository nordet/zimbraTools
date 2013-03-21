# -*- coding: utf-8 -*-
# Create your views here.
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.http import Http404
from django.core.urlresolvers import reverse
from forms import UploadFileForm
from django.conf import settings
from icalendar.parser import Contentline
from icalendar import Calendar, Event
from icalendar.parser import *
from icalendar.cal import *
from enchant.utils import str
from forms import SelectCompteForm
from forms import SelectCalendarForm
from tools import list2tuple
from django.template.context import Context
import time
from zimbraTools.settings import ZIMBRA_SERVER, MEDIA_ROOT
import os
from rope.base.builtins import Str
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.encoding import smart_str
# from rope.base.builtins import Str


ficEntree = ""
ficSortie = ""

def fichierEntree(f):
  return getattr(settings, "MEDIA_ROOT", None) + str(f)

def fichierSortie(f):
  return getattr(settings, "MEDIA_ROOT", None) + 'clean_' + str(f)

def handle_uploaded_file(f):
  with open(ficEntree, 'wb+') as destination:
    for chunk in f.chunks():
      destination.write(chunk)

def sameEvents (event1, event2):
  """
  This function determines if the two events pass by parameter are equal or not.
  We compare each property of the events. We exclude properties UID, DTSTAMP and LAST-MODIFIED.
  """
  eventsAreEqual = True
  if len(event1.property_items(recursive=False)) <> len(event2.property_items(recursive=False)):
    eventsAreEqual = False
  else:
    for prop1 in event1.property_items(recursive=False):
      for prop2 in event2.property_items(recursive=False):
        if ((prop1[0] == prop2[0]) and 
            (prop1[0] != "DTSTAMP") and (prop1[0] != "UID") 
            and (prop1[0] != "LAST-MODIFIED")):
          if ((prop1[0] == "DTSTART") or (prop1[0] == "DTEND")):
            if (prop1[1].to_ical() != prop2[1].to_ical()):
              eventsAreEqual = False
          else:
            if prop1[1] != prop2[1]:
              eventsAreEqual = False
  return eventsAreEqual

def cleanFileIcs(fEntree, fSortie):
  cal = Calendar.from_ical(open(fEntree, 'rb').read())
  cleanCal = Calendar()
  #
  # We initialize the clean calendar with previous calendar's attributes
  for prop in cal.walk()[0].property_items(recursive=False):
    if prop[0] != 'BEGIN' and prop[0] != 'END': cleanCal.walk()[0][prop[0]] = prop[1]

  for i in range(1, len(cal.walk()) - 1):
    trouve = False
    for j in range(len(cleanCal.walk())):
      if sameEvents(cal.walk()[i], cleanCal.walk()[j]):
        trouve = True
        break
    if not trouve:
      cleanCal.add_component(cal.walk()[i])
      
  open(fSortie, 'wb').write(cleanCal.to_ical())

def cleanFileIcs2(fEntree, fSortie):
  f = open('/tmp/debug.txt', 'w')
  cal = Calendar.from_ical(open(fEntree, 'rb').read())
  #
  # We initialize the clean calendar with previous calendar's attributes
  tailleCal = len(cal.walk())
  f.write("====== Contenu de cal =========\n")
  for i in range(len(cal.walk())):
    f.write("cal.walk() [" + str(i) + "] = " + str(cal.walk()[i]) + "\n")
  f.write("====== Traitement de cal =========\n")
  i = 0
  while i < len(cal.walk()):
    j = i + 1
    while j < tailleCal:
      f.write("===== cleanFileIcs2 : tailleCal = " + str(tailleCal) + "\n")
      f.write("===== cleanFileIcs2 : cal.walk()[" + str(i) + "] = " + str(cal.walk()[i]) + "\n")
      f.write("===== cleanFileIcs2 : cal.walk()[" + str(j) + "] = " + str(cal.walk()[j]) + "\n")
      if sameEvents(cal.walk()[i], cal.walk()[j]):
        # f.write("===== cleanFileIcs2 : Avant suppression de cal.walk()[" + str(j + 1) + "] = " + str(cal.walk()[j + 1]) + "\n")
        f.write("===== cleanFileIcs2 : suppression de " + str(j) + " = " + str(cal.walk()[j]) + "\n")
        del(cal.walk()[j])
        f.write("===== cleanFileIcs2 : Après suppression de cal.walk()[" + str(j) + "] = " + str(cal.walk()[j]) + "\n")
        # f.write("===== cleanFileIcs2 : Après suppression de cal.walk()[" + str(j + 1) + "] = " + str(cal.walk()[j + 1]) + "\n")
        # tailleCal = tailleCal - 1
      j += 1
    i += 1
    
  tailleCal = len(cal.walk())
  f.write("====== Contenu de cal =========\n")
  for i in range(len(cal.walk())):
    f.write("cal.walk() [" + str(i) + "] = " + str(cal.walk()[i]) + "\n")
  f.close()
  open(fSortie, 'wb').write(cal.to_ical())

def cleanFileIcs3(fEntree, fSortie):
  cal = Calendar.from_ical(open(fEntree, 'rb').read())
  # lcal = list(cal.walk)
  fini = False
  i = 0
  while not fini :
    j = i + 1
    while j < len(cal.walk()):
      if sameEvents(cal.walk()[i], cal.walk()[j]):
        cal.del_component(cal.walk()[j])
      else:
        j = j + 1
    if i == len(cal.walk()) - 1:
      fini = True
    else:
      i += 1
  open(fSortie, 'wb').write(cal.to_ical())

def fileToClean(request):
  global ficEntree
  global ficSortie
  if request.method == 'POST':
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
      fichier = request.FILES['file']
      ficEntree = fichierEntree(fichier)
      ficSortie = fichierSortie(fichier)
      handle_uploaded_file(fichier)
      cleanFileIcs(ficEntree, ficSortie)
      response = HttpResponse(mimetype='application/force-download')
      ficSortie = 'clean' + str(fichier)
      response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(ficSortie)
      response['X-Sendfile'] = smart_str(getattr(settings, "MEDIA_ROOT", None))
      # It's usually a good idea to set the 'Content-Length' header too.
      # You can also set any other required headers: Cache-Control, etc.
      return response
  else:
    form = UploadFileForm()
    return render_to_response('fileToCleanForm.html',
                              {'form': form},
                              context_instance=RequestContext(request))

def fileCleanAgenda(request):
    return render_to_response('fileCleanAgenda.html', {'fichierSortie': fichierSortie, })

@login_required
def select_compte(request):
  if request.method == 'POST':
    form = SelectCompteForm(request.POST, request.FILES)
    if form.is_valid():
      compte = form.cleaned_data['compte']
      if isinstance(compte, unicode):
        compte = compte.encode('ascii', 'ignore')
      # request.session['current_account'] = compte
    return HttpResponseRedirect(reverse('calendarToClean', args=[compte]))
  else:
    form = SelectCompteForm()
    return render_to_response('select_compte.html',
                              {'form': form, },
                              context_instance=RequestContext(request))

def calendarToClean(request, compte):
  # compte = request.session['current_account']
  if request.method == 'POST':
    queryDictRequestPost = request.POST.copy()
    queryDictRequestPost.appendlist('compte', compte)
    form = SelectCalendarForm(queryDictRequestPost)
    
    # if form.is_valid():
    # calendrier = form.cleaned_data['calendrier']
    calendrier = queryDictRequestPost['calendrier']
    #
    # export du calendrier
    cpte = compte.encode('ascii', 'ignore')
    if isinstance(calendrier, unicode):
      calendrier = calendrier.encode('ascii', 'ignore')
    ficExport = "calExport_" + cpte + "_" + calendrier + "_" + time.strftime('%d-%m-%y_%H:%M', time.localtime()) + ".ics"
    commande = "ssh root@" + ZIMBRA_SERVER + " /root/zimbraTools/exporterCalendar.sh " + cpte + " " + calendrier + " " + ficExport
    os.popen(commande)
    #
    # copie du fichier calendrier en local
    commande = "scp root@" + ZIMBRA_SERVER + ":/tmp/zimbraTools/" + ficExport + " " + MEDIA_ROOT
    os.popen(commande)
    ficClean = "clean_" + ficExport
    ficEntree = fichierEntree(ficExport)
    ficSortie = fichierSortie(ficExport)
    #
    # nettoyage des doublons dans le fichier importé
    cleanFileIcs(ficEntree, ficSortie)
    #
    # copie du fichier nettoyé sur le serveur zimbra
    commande = "scp " + MEDIA_ROOT + ficClean + " root@" + ZIMBRA_SERVER + ":/tmp/zimbraTools/"
    os.popen(commande)
    #
    # Suppression du contenu du calendrier Zimbra en cours
    commande = "ssh root@" + ZIMBRA_SERVER + " /root/zimbraTools/clearCalendar.sh " + cpte + " " + calendrier
    os.popen(commande)
    #
    # Import du fichier calendrier nettoyé dans le calendrier Zimbra en cours
    commande = "ssh root@" + ZIMBRA_SERVER + " /root/zimbraTools/importerCalendar.sh " + cpte + " " + calendrier + " " + ficClean
    os.popen(commande)
    #
    # Suppression des fichiers temporaires
    os.remove(MEDIA_ROOT + ficExport)
    os.remove(MEDIA_ROOT + ficClean)
    commande = "ssh root@" + ZIMBRA_SERVER + " rm /tmp/zimbraTools/" + ficExport
    os.popen(commande)
    commande = "ssh root@" + ZIMBRA_SERVER + " rm /tmp/zimbraTools/" + ficClean
    os.popen(commande)
    # return HttpResponse("Nettoyage du calendrier effectué !")
    messageType = "success"
    message = "Nettoyage du calendrier effectué !"
    return render_to_response('message.html', {'STATIC_URL': settings.STATIC_URL,
                                                 'messageType': messageType, 'message': message})
    # return HttpResponseRedirect(reverse('message', args=(messageType, message,)))
  else:
    form = SelectCalendarForm(compte)
    return render_to_response('calendarCompteToClean.html',
                              {'compte': compte, 'form': form, },
                              context_instance=RequestContext(request))

def login_interne(request):
  username = request.POST['username']
  password = request.POST['password']
  user = authenticate(username=username, password=password)
  if user is not None:
    if user.is_active:
      login(request, user)
      return HttpResponseRedirect(reverse('home'))
    else:
      # return HttpResponse("Compte inexistant !")
      messageType = "warning"
      message = "Compte inexistant !"
      return render_to_response('message.html', {'STATIC_URL': settings.STATIC_URL,
                                                 'messageType': messageType, 'message': message})
  else:
    # return HttpResponse("Identifiant ou mot de passe incorrect !")
    messageType = "warning"
    message = "Identifiant ou mot de passe incorrect !"
    return render_to_response('message.html', {'STATIC_URL': settings.STATIC_URL,
                                               'messageType': messageType, 'message': message})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def home(request):
  if request.user.is_authenticated():
    # return HttpResponse("Connecté !")
    return HttpResponseRedirect(reverse('select_compte'))
  else:
    # return HttpResponse("Non connecté !")
    return HttpResponseRedirect(reverse('fileToClean'))

def message(request, messageType, message):
    return render_to_response('message.html')

