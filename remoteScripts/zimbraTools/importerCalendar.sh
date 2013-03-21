#!/bin/bash
retour=$(su -l zimbra -c 'zmmailbox -z -m '$1' postRestUrl "/'$2'?fmt=ics&resolve=reset" /tmp/zimbraTools/'$3)
echo $retour


