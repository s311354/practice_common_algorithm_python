"""
File: TextMeWhenItsDone.py
Description: 
"""
import smtplib
import csv

GMAIL = "gmail.com"

Message = """Subject: Program Confirmation
To: {recipient}
From: {sender}

Hey, Thanks for your waiting! Your program is done. We are processing it now and will contact you soon"""


class TextMeWhenItsDone(object):
    """
    A :class:~practice_common_algorithm.tool.TextMeWhenItsDone object is the sending an email module

    The smtplib module defines an SMTP client session object that can be used to send mail to any internet machine with an SMTP or ESMTP listener daemon.

    """
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
        if email[email.index("@")+1:] == GMAIL:
            server = smtplib.SMTP("smtp.gmail.com", 587)

        server.starttls()
        server.login(email, password)
        server.sendmail(email, receiver, Message.format(recipient=receiver, sender=email, name="Yo"))
