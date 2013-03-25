# -*- coding: utf-8 -*-
'''
Created on 21 févr. 2013

@author: pascal
'''
import os
from rope.base.builtins import Str

class ComptesZimbra():
  def __init__(self, zimbraServer=None):
    proces = os.popen("ssh root@" + str(zimbraServer) + " /root/zimbraTools/recuperationComptesZimbra.sh")
    chaine = proces.read()
    print "===== ComptesZimbra : zimbraServer = ", zimbraServer
    print "===== ComptesZimbra : chaine = ", chaine
    self.liste = chaine.split()
