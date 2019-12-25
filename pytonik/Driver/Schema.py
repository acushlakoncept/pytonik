# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 08/11/2019.

from pytonik.Driver.DB.support import Table #Select, Delete, Insert, Update, 


class Schema:

    def __getattr__(self, item):
        return item
    
    def __init__(self):
        return None
    
    def table(self, table):
        return Table.Table(table)
    
        
        