#!/usr/bin/env python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
x = s.getsockname()[0]

s.close()
c = socket.gethostname()
string = c + " is UP, IP address is " + x

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = "andyrocket3meuk@gmail.com"
toaddr = "71v6qc8a9w@pomail.net"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr

msg['Subject'] = string
body = "The Pi is starting up"
msg.attach(MIMEText(body, 'plain')) # redundant parentheses

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "qfcpuqccmgwpiztd")

text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

print("Push sent")
