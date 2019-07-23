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

message = ""
# Code to get the highlights and organise them into message is going to go there

# setup the parameters of the message
msg['From']=email_address
msg['To']=str(input('Enter email address of the receiver: '))
msg['Subject']="Your daily highlights"

# add-in the message body
msg.attach(MIMEText(message))

# send the message via the server set up earlier.
s.send_message(msg)

del msg

s.quit()
