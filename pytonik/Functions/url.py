# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 05/11/2019.
import os


class url():
    def __getattr__(self, item):
        return item

    def __init__(self, *args, **kwargs):
        print(**kwargs)
        return None




    def path(self, path = "", public = ""):
        DS = str('/')
        if path[:1] == "/" or public[:1] == "/":
            DS = ""
        else:
            DS = "/"

        if path != "":
            return  DS + path
        elif  public !=  "":
            return DS+'public' + DS + public



    def url(self, path = ""):
        http = os.environ.get("HTTPS")
        if http == 'on':
            url = str("https://") + os.environ.get("HTTP_HOST")
        else:
            url = str("http://") + os.environ.get("HTTP_HOST")
        DS = ""
        if path == "":
            DS = ""
        else:
            if path[:1] == "/":
                DS = ""
            else:
                DS = "/"
        return url + DS + path[1:]


