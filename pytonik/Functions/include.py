# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 08/11/2019.

from pytonik.Editor import HTMLeditor
from pytonik.Log import Log
from pytonik.App import App
import os
log_msg = Log()
Ap = App()

class include():

    def __getattr__(self, item):
        return item

    def __init__(self, *args, **kwargs):

        return  None

    def include(self, *args, **kwargs):
        host = os.path.dirname(os.getcwd())
        DS = str("/")
        pth = ""
        for v in args:
            pth = v

        split = pth.split('.')

        fileExists = []
        for x in split:
            fileExists.append(x)

        try:

            dirF =  list(filter(None, fileExists))
            lf = ""
            for v in dirF:
                lf +="/"+v

            template_dir = host + DS + 'views' + lf
            engine  = template_dir.rsplit('/', 1)[-1]
            direct = template_dir.rsplit('/', 1)[-2]

            if os.path.isdir(direct) == True:

                if os.path.isfile(template_dir+".html") == True:
                    loadm0 = Ap.loadmodule()
                    return self.read_html(direct, engine, loadm0)
                else:
                  log_msg.error("The File '{filepath}' does not exists.".format(filepath=template_dir+".html"))
                  return "The File '{filepath}' does not exists.".format(filepath=template_dir+".html" )

            else:
              log_msg.error("The Folder '{filepath}' does not exists.".format(filepath=direct))
              return "The Folder '{filepath}' does not exists.".format(filepath=direct)

        except Exception as err:
                log_msg.error(err)
                return  err


    def read_html(self, template_dir, engine, context=[]):

        html_file_path = os.path.join(template_dir, "%s.html" % engine)

        try:
            with open(html_file_path) as html_file:
                html = html_file.read()
            return HTMLeditor.Template(html).render(**context)
        except Exception as err:
            log_msg.error(err)


