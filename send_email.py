import smtplib, ssl
import os

def send_email(topic,raw_message,user_email):
    host = 'smtp.gmail.com'
    port = 465
    recipient = 'boyercoding@gmail.com'
    recipient_password = os.getenv('PASSWORD')

    message = f"""\
Subject: Company Website

From: {user_email}
{topic}: {raw_message}
"""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(recipient, recipient_password)
        server.sendmail(user_email,recipient,message)
