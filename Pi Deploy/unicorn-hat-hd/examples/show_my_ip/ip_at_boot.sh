sudo cp show_my_ip.service /etc/systemd/system/
mkdir -p /home/pi/daemon
cp show_my_ip.py /home/pi/daemon
sudo systemctl enable show_my_ip.service
sudo systemctl start show_my_ip.service
