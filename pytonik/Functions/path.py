# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 05/11/2019.
import os



class path:

    def __getattr__(self, item):
        return item

    def __init__(self, *args,  **kwargs):

        self.ul = self.path(*args, **kwargs)
        return None

    def __str__(self):

        return self.ul

    def path(self, path = "", link = ''):
        DS = str('/')
        u = ""
        if path[:1] == DS or path[:1] == DS:
            DS = ""
        else:
            DS = "/"
        if link == 'True':
            u = self.url()

        return u + DS + path



    def url(self):
        http = os.environ.get("HTTPS")
        if http == 'on':
            url = str("https://") + os.environ.get("HTTP_HOST")
        else:
            url = str("http://") + os.environ.get("HTTP_HOST")

        return url



