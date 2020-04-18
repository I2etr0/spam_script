#!/usr/bin/python3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def sendMail():
    msg = MIMEMultipart()

    # General settings
    msg['from'] = 'form@example.com'
    msg['to'] = 'to@example.com'
    msg['subject'] = 'your_subject'
    message = 'your_messages'

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # Create server
    server = smtplib.SMTP('yourmailserver:port')

    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print("Successfully send mail to %s:" % (msg['to']))


def spam():

    min = 1
    max = int(input('How much messages you want send: '))

    while max >= min:
        sendMail()
        min += 1


spam()
