import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from highlights import get_library

s = smtplib.SMTP(host='smtp.office365.com', port=587)
#s = smtplib.SMTP(host='smtp.gmail.com', port=465) for gmail address

s.starttls()

email_address = # enter the email address from which the mail will be sent
password = # enter the password of this address

#login to your email account
s.login(email_address, passsword)

# create a message
msg = MIMEMultipart()

message = ""
# Code to get the highlights and organise them into message is going to go there
library = get_library()

# setup the parameters of the message
msg['From'] = email_address
msg['To'] = email_address # you can change this address to the address you want to receive the email
msg['Subject']= "Your daily highlights" # change the subject of the email if you want

# add in the message body
msg.attach(MIMEText(message))

# send the message via the server set up earlier.
s.send_message(msg)

del msg

s.quit()
