# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 08/01/2020.
import re
from pytonik.Functions.validation import validation

class iteration(validation):


    def __getattr__(self, item):

        return item

    def __call__(self, *args, **kwargs):

        return None

    def __init__(self, *args,  **kwargs):
        return None


    def iteri(self, dictionary="", itr="pid"):

        i = 0
        if dictionary is not "" or dictionary is not None:
            dist, apend = [], []
            for l in dictionary:
                i += 1
                ++i
                listv = l
                dist = {itr: i}
                dist.update(listv)
                apend.append(dist)
            return apend



    def keyword(self, keywords, url="/", css=['']):

        pattern = re.compile("\s*,\s*|\s+$")
        splittag = [x for x in pattern.split(keywords) if x]
        for keyword in splittag:
            return '<a href="{url}" class="{css}">{keyword}</a>'.format(url= url, css = css[0], keyword= str(keyword))
