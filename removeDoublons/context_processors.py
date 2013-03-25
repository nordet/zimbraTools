# -*- coding: utf-8 -*-
'''
Created on 25 mars 2013

@author: pascal
'''
def currentZimbraServer(request):
  if 'currentZimbraServer' in request.session:
    return {'currentZimbraServer' : request.session['currentZimbraServer'] }
  else:
    return {'currentZimbraServer' : '' }
