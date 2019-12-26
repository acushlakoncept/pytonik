# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 08/11/2019.

from pytonik.App import App

app = App()

class Schema:

    def __getattr__(self, item):
        
        return item
    
    def __init__(self):
        app.DB()
        self.driver = app.Driver
        return None
    
    def table(self, table):
        
        if self.driver == "MYSQL":
            from pytonik.Driver.DB.MYSQL.Table import  Table
            return Table(table)
        
        if self.driver == "Oracle":
            from pytonik.Driver.DB.Oracle.Table import  Table
            return Table(table)
        
        if self.driver == "pyPgSQL":
            from pytonik.Driver.DB.pyPgSQL.Table import  Table
            return Table(table)
    
          
        if self.driver == "SQLite":
            from pytonik.Driver.DB.SQLite.Table import  Table
            return Table(table)
    
        
        