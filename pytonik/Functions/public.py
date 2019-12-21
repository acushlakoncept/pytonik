# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 09/11/2019.


class public():
    def __getattr__(self, item):
        return item

    def __init__(self, *args, **kwargs):

        return None

    def path(self, public = ""):
        DS = str('/');

        if public == "/":
            DS = ""
        else:
            DS = "/"
        return DS + 'public' + DS + value

