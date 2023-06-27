import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email import encoders

msg = MIMEMultipart()
msg['From'] = 'xxxx'
msg['To'] = 'xxxx'
msg['Subject'] = 'Python Test'

msgtext = 'Hello world! So stupid...'

msg.attach(MIMEText(msgtext,'plain'))

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('xxxx','xxxx')
server.send_message(msg)
server.quit()