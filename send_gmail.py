#!/usr/bin/env python
import argparse, sys, smtplib
from email.mime.text import MIMEText

# if __name__ == "__main__":
parser = argparse.ArgumentParser(description='Python Gmail sender')
parser.add_argument('-u','--user', help='Gmail sender username', required=True)
parser.add_argument('-p','--password', help='Gmail sender password', required=True)
parser.add_argument('-t','--to', help='Mailto email address', required=True)
parser.add_argument('-f','--fromaddr', help='Mailfrom email address', required=False)
parser.add_argument('-s','--subject', help='Email subject', required=False)
parser.add_argument('-b','--body', help='Email body', required=False)
args = parser.parse_args()

msg = MIMEText(args.body)
msg['Subject'] = args.subject
msg['To'] = args.to
msg['From'] = args.fromaddr if args.fromaddr else args.user

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo_or_helo_if_needed()
server.starttls()
server.ehlo_or_helo_if_needed() # call again according to python docs
server.login(args.user, args.password)

try:
  server.sendmail(args.user, args.to, msg.as_string())
except SMTPRecipientsRefused:
  print "All recipients were refused. Nobody got the mail."
except SMTPHeloError:
  print "The server did not reply properly to the HELO greeting"
except SMTPSenderRefused:
  print "The server did not accept the from address."
except SMTPDataError:
  print "The server replied with an unexpected error code (other than a refusal of a recipient)."
else:
  print "email sent!"
finally:
  server.quit()