import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

s = smtplib.SMTP(host='smtp.office365.com', port=587)
#s = smtplib.SMTP(host='smtp.gmail.com', port=465) for gmail address

s.starttls()

email_address = str(input('Enter your email address: '))
password = str(input('Enter your password: '))

#login to your email account
s.login(email_address, passsword)

# create a message
msg = MIMEMultipart()

