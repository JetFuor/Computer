import smtplib
from email import encoders, message
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
server = smtplib.SMTP('smtp.gmail.com', 587, None, 30)

server.ehlo()
server.starttls()


with open('password.txt', 'r') as f:
    password = f.read()

server.login('testingstuff034@gmail.com', password)

msg = MIMEMultipart()
msg['From'] = 'Stephen'
msg['To'] = 'testing@spaml.de'
msg['Subject'] = 'Test'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

text = msg.as_string()
server.sendmail('testingstuff034@gmail.com', 'testing@spaml.de', text)