# -*- coding: utf-8 -*-
'''
Created on 21 févr. 2013

@author: pascal
'''
import os

class CalendriersCompteZimbra():
  def __init__(self, compte=None, zimbraServer=None):
    # commande = "ssh root@" + "mail.nordet.org" + " /root/zimbraTools/recuperationRepertoiresCompte.sh " + Str(compte)
    # print "===== CalendriersCompteZimbra : commande = ", commande
    proces = os.popen("ssh root@" + str(zimbraServer) + " /root/zimbraTools/recuperationRepertoiresCompte.sh " + compte)
    chaine = proces.read()
    self.liste = chaine.split("/")
