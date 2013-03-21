#!/bin/bash
repertoires=$(su -l zimbra -c 'zmmailbox -z -m '$1' gaf|grep appo|cut -c 43-|grep "(" -v')
echo $repertoires


