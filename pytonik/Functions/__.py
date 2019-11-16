# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 07/11/2019.

from pytonik.Lang import Lang
from pytonik.Router import Router

class __():

    def __getattr__(self, item):
        return item

    def __init__(self, *args, **kwargs):

        self.langs = Lang(Router().getLanguages())
        self.langs.loadLang()
        return None


    def lang(self, lang="", defindValue = ''):

        if lang is not "":
            return self.langs.get(lang, defindValue)



