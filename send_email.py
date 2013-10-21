#!/usr/bin/python
 
import smtplib
import sys
 
fromaddr = 'cultura.alerts@gmail.com'
toaddrs  = sys.argv[1]
msg = 'cultura is dry!'
 
# Credentials (if needed)
username = 'cultura.alerts@gmail.com'
password = 'cultura1'
 
# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
