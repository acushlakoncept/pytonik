###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###


def App():
    from . import App
    return App.App()

def Config():
    from . import Config as Config
    return Config.Config()



def Helpers():
    from .Core import Helpers
    return Helpers

def Session():
    from .Session import Session
    return Session()

def Request():
    from .Request import Request
    return Request()

def Hash():
    from .Hash import Hash
    return Hash()

def Model():
    from .Model import Model
    M = Model()
    return M

def Load(m):
    M = Model()
    return M.load(m)

def Functions():
    from .Core import Functions
    return Functions

def File():
    from .Core import File

    return File

def SendEmail(from_send, to_recipient, message_subject= "", messege_content = ""):
    from .Core.SMTP import SMTP

    return SMTP().send(from_send, to_recipient, message_subject, messege_content)

def Logs():
    from .Log import Log

    return Log()


def url(path=""):
    import os
    http = os.environ.get("HTTPS")
    if http == 'on':
        url = str("https://") + os.environ.get("HTTP_HOST")
    else:
        url = str("http://") + os.environ.get("HTTP_HOST")

    return url + path