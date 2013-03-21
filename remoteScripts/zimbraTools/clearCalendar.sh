#!/bin/bash
retour=$(su -l zimbra -c 'zmmailbox -z -m '$1' ef /'$2)
echo $retour


