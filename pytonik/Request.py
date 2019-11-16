###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###



import cgi, re, os
from . import App, Router, Log
log_msg = Log.Log()

class Request:
    def __init__(self):
        self.attr = cgi.FieldStorage()
        self.type = os.environ
        self.Router = Router.Router()


    def get(self, key=0, error=0):
        try:
            if 'GET' in self.type.get('REQUEST_METHOD'):

                if key != 0:
                    if (key in self.attr):
                        return self.attr.getvalue(key)
                    elif error == 1:
                        return self.attr
                    else:
                        return ""
                else:
                    return ""
            else:
                print("advise use POST instead of GET")
        except Exception as err:
            log_msg.info(err)
            return  err

    def post(self, key=0, error=0):
        try:
            if 'POST' in self.type.get('REQUEST_METHOD'):
                if key != 0:
                    if (key in self.attr):
                        return self.attr.getvalue(key)
                    elif error == 1:
                        return self.attr
                    else:
                        return ""
                else:
                    return ""
            else:

                print("advise use GET instead of POST")
        except Exception as err:
            log_msg.info(err)
            return err

    def file(self, key=0, error=0):
        try:
            if key != 0:
                if (key in self.attr):
                    self.attr.getvalue(key)
                    return self.attr[key]
                elif error == 1:
                    return self.attr
                else:
                    return ""
            else:
                return ""

        except Exception as err:
            log_msg.info(err)
            return err

    def all(self):
        if None is not self.attr.keys():
            return self.attr.keys()

    def params(self, key=0):
        try:
            if 'POST' in self.type.get('REQUEST_METHOD'):

                print("advise use GET or POST instead of PARAMS")
            else:
                para = self.Router.getParams()

                if para != "" or para is not None:
                    for k in para.keys():
                        if key in para:
                            if para[k] != "" or para[k] is not None:
                                return para[k]
                            return ""
                    return ""
                else:
                    return self.get(key)

        except Exception as err:
            log_msg.info(err)

    def strig_tag(self, value=""):
        if value != "":

            return re.sub('<[^<]+?>', '', value)
        else:
            return ""
