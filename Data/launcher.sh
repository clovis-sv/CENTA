#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute python script, then back home

cd /

# uncomment for CENTA's RPi
cd home/pi/CENTA/Data

# uncomment for German RPi
#cd home/pi/projects/Data

sudo python FS.py
cd /



