###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###
import os
from pytonik import Log
from pytonik import Version
import ast

log_msg = Log.Log()


class Lang:

    def __init__(self, lg):
        self.data = ""
        self.lg = lg


    def loadLang(self):

        host = os.path.dirname(os.getcwd())
        DS = str("/")

        langpath = host + DS + 'lang'+DS+self.lg.lower() +".py"
        try:
            if os.path.isfile(langpath) == True:

                with open(langpath, 'rb') as rb:
                    self.data = rb.read().decode('utf-8')
                return self.data

        except Exception as e:
            log_msg.error("Lang file not found {}".format(e))
            return "Lang file not found {}".format(e)



    def get(self, key, defindValue = ''):
        data = ast.literal_eval(self.data)

        if Version.PYVERSION_MA <= 2:
            items = data.iteritems()
        else:
            items = data.items()

        if key in data:
            for k, v in items:
                return data[k.lower()]
        else:
            return defindValue
