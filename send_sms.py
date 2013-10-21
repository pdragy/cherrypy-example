import smtplib,sys
number = sys.argv[1]
carrier = sys.argv[2]

user = 'cultura.alerts@gmail.com'
password = 'cultura1'

if "T-Mobile" in carrier:
	ext = "@tmomail.net"
elif "AT&T" in carrier:
	ext = "@txt.att.net"
elif "Verizon" in carrier:
	ext = "@vtext.com"
elif "Sprint" in carrier:
	ext = "@messaging.sprintpcs.com"
elif "MetroPCS" in carrier:
	ext = "@mymetropcs.com"
elif "US Cellular" in carrier:
	ext = "@email.uscc.net"
elif "C Spire" in carrier:
	ext = "@cspire1.com"
elif "Cincinnati Bell" in carrier:
	ext = "@gocbw.com"

server = smtplib.SMTP( "smtp.gmail.com", 587 )
server.starttls()
server.login(user, password )
server.sendmail( 'alert', number + ext, 'cultura is dry!' )
