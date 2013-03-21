# -*- coding: utf-8 -*-
'''
Created on 21 févr. 2013

@author: pascal
'''
import os
from zimbraTools.settings import ZIMBRA_SERVER


class ComptesZimbra():
  def __init__(self):
    proces = os.popen("ssh root@" + ZIMBRA_SERVER + " /root/zimbraTools/recuperationComptesZimbra.sh")
    chaine = proces.read()
    self.liste = chaine.split()
