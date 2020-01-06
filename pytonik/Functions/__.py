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
        self.lg = self.lang(*args, **kwargs)
        return None

    def __str__(self):

        return self.lg


    def lang(self, lang="", defindValue = ''):

        if lang is not "":
            return self.langs.get(lang, defindValue)



    def default(self):

        return self.langs.lg