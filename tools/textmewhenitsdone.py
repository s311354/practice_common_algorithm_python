"""
File: TextMeWhenItsDone.py
Description: 
"""
import smtplib
import csv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage


GMAIL = "gmail.com"

Message = """Subject: Program Confirmation
To: {recipient}
From: {sender}

Hey, Thanks for your waiting! Your program is done. We are processing it now and will contact you soon

Regards
Shi-rong (Louis) Liu
http://louiscode00.com/
"""


class TextMeWhenItsDone(object):
    """
    A :class:~practice_common_algorithm.tool.TextMeWhenItsDone object is the sending an email module

    The smtplib module defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon.

    """

    def __init__(self, email):
        if email[email.index("@")+1:] == GMAIL:
            self.server = smtplib.SMTP("smtp.gmail.com", 587)

    def TextMe(self, email, password, receiver="YO"):
        """ Simple Mail Transfer Protocal is an application layer protocol in the OSI model.

        :param email:  The address sending this email
        :type  email:  string

        :param password:  The password for the authentication
        :type  password:  string

        :param receiver:  A list of addresses to send this mail to
        :type  receiver:  string

        :return:  Description
        :rtype:  Type

        """

        self.server.starttls()
        self.server.login(email, password)
        self.server.sendmail(email, receiver, Message.format(recipient=receiver, sender=email))

    def TextMeImage(self, email, password, receiver="YO"):
        """docstring for TextMeImage"""

        msg = MIMEMultipart('alternative')
        msg['Subject'] = "subject"
        msg['From'] = email
        msg['To'] = receiver

        text = MIMEText('<img src="cid:image1">', 'html')
        msg.attach(text)

        image1 = MIMEImage(open('./Pictures/71704880_2928981783782886_1021381306463813632_n.jpeg', 'rb').read())

        # Define the image's ID as referenced in the HTML body above
        image1.add_header('Content-ID', '<image1>')
        msg.attach(image1)

        if email[email.index("@")+1:] == GMAIL:
            server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()
        server.login(email, password)
        server.sendmail(email, receiver, msg.as_string())
        server.quit()
