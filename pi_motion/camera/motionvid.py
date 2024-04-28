#!/usr/bin/env python

import smtplib

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

fromaddr = "YOUR EMAIL"
toaddr = "EMAIL ADDRESS YOU SEND TO"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Motion Cam Activated"
body = "Video of Motion Detected"
msg.attach(MIMEText(body, 'plain'))

import os
rootpath = '/var/lib/motion'
filelist = [os.path.join(rootpath, f) for f in os.listdir(rootpath)]
filelist = [f for f in filelist if os.path.isfile(f)]
newest = max(filelist, key=lambda x: os.stat(x).st_mtime)
filename = newest

import os
rootpath = '/var/lib/motion'
filelist = [os.path.join(rootpath, f) for f in os.listdir(rootpath)]
filelist = [f for f in filelist if os.path.isfile(f)]
newest = max(filelist, key=lambda x: os.stat(x).st_mtime)
attachment = open(newest, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "YOUR PASSWORD")
text = msg.as_string()

server.sendmail(fromaddr, toaddr, text)

server.quit()