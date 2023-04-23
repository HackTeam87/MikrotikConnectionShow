#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin
cd /home/grin/app/MikrotikConnectionShow/ && gunicorn -w 1 run:app -b :5555 --timeout 600  --access-logfile /home/grin/app/MikrotikConnectionShow/log

#--log-level debug
