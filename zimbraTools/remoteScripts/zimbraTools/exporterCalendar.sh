#!/bin/bash
if ! test -d /tmp/zimbraTools; then
  su -l zimbra -c 'mkdir /tmp/zimbraTools'
fi

retour=$(su -l zimbra -c 'zmmailbox -z -m '$1' getRestUrl "/'$2'?fmt=ics" > /tmp/zimbraTools/'$3)
echo $retour


