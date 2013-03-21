# -*- coding: utf-8 -*-
def list2tuple (liste):
  t = []
  for e in liste:
    if e != '':
      t.append((e.strip(), e.strip()))
  return t
