#!/usr/bin/env python

import smtplib

from datetime import datetime
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

fromaddr = "YOURADDRESS"
toaddr = "RECIEVINGADDRESS"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Motion Detected"
body = 'A motion has been detected.\nTime: %s' % str(datetime.now())
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "YOURPASSWORD")
text = msg.as_string()

server.sendmail(fromaddr, toaddr, text)

server.quit()
