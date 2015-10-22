#!/bin/bash
python manage.py runfcgi pidfile=$PWD/process.pid host=127.0.0.1 port=8088 --settings=tem.settings outlog=/tmp/out.log errlog=/tmp/err.log debug=True

