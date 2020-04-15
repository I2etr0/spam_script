#!/usr/bin/python3
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


def sendMail():
    msg = MIMEMultipart()

    # General settings
    msg['from'] = 'example@mail.com'
    msg['to'] = 'yourmail@mail.com'
    msg['subject'] = 'Your subject'
    message = 'Your message'

    # add in the message body
    msg.attach(MIMEText(message, 'plain'))

    # Create server
    server = smtplib.SMTP('app-carrier-0.cloud.platiza.ru:25')

    # send the message via the server.
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    server.quit()

    print("Successfully send mail to %s:" % (msg['to']))


def spam():
    i = input('Insert your number')
    while i > 1:
        sendMail()
        i -= 1


spam()
