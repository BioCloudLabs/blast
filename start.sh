#!/bin/bash

chmod 666 /var/run/docker.sock
/usr/sbin/apache2ctl -D FOREGROUND