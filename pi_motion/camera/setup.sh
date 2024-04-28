#!/bin/bash

mkdir ~/daemon
cp ~/pi_motion/camera/email_on_up.py ~/daemon
cp ~/pi_motion/camera/on_boot.sh ~/daemon

/home/pi/daemon/on_boot.sh
