###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###


import smtplib, string, random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .. import Router, Config, Log
log_msg = Log.Log()


class SMTP():

    def __init__(self):

        self.Router = Router.Router()
        self.envSMTP = self.Router.env()

        Conf = Config.Config()

        Conf.add(self.envSMTP)
        setting = Conf.get('SMTP')
        self.server = setting['server']
        self.port = setting['port']
        self.username = setting['username']
        self.password = setting['password']

        self.con = None
        self.result = None
        self.response = None
        self.connect()
        return None

    def connect(self):
        try:
            self.response = smtplib.SMTP(self.server, self.port)
            self.response.starttls()
            self.response.login(self.username, self.password)
            return self.response
        except Exception as err:
            log_msg.error(err)

    def close(self):
        return self.response.quit()


    def send(self, from_send, to_recipient, message_subject= "", messege_content = ""):
        print(self.response)
        try:
            body = messege_content
            msg = MIMEMultipart()
            msg['From'] = from_send
            msg['To'] = to_recipient
            msg['Subject'] = message_subject
            msg.attach(MIMEText(body, 'html'))
            context = msg.as_string()
            self.response.sendmail(from_send, to_recipient, context)
            self.close()
            return True
        except Exception as err:
            log_msg.error(err)
            return err

