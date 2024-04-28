#!/bin/bash
sudo cp binary_clock_uni_at_boot.service /etc/systemd/system/binary_clock_uni_at_boot.service
mkdir -p /home/pi/daemon/
sudo cp binary_clock_uni.py /home/pi/daemon/binary_clock_uni.py
sudo systemctl enable binary_clock_uni_at_boot.service
sudo systemctl start binary_clock_uni_at_boot.service
