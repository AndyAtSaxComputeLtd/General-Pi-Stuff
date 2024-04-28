#!/usr/bin/env python
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print("Email Sent")
x = s.getsockname()[0]
s.close()

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = "andyrocket3meuk@gmail.com"
toaddr = "andy@arh.me.uk"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "IP Address"
body = "IP Address is :" + x
msg.attach(MIMEText(body, 'plain')) # redundant parentheses

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "qfcpuqccmgwpiztd")

text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

