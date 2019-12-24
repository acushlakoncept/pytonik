# Author : BetaCodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by BetaCodings on 08/11/2019.

from pytonik import Log
import os, sys
log_msg = Log.Log()
host = os.path.dirname(os.getcwd())
D = "/"
try:
    import sqlite3

except Exception as err:
    log_msg.critical(err)


class SQLite:

    def __init__(self, setting):
        self.path = setting['path']
        self.name = setting['name']
        self.bdfile = str(host) + D + str(self.path)+ D +str(self.name)
        self.rollback = ""
        self.success = ""
        self.conn = None
        self.con = None
        self.result = None
        self.connectDB()
        

    def connectDB(self):

        try:
            self.conn = sqlite3.connect(self.bdfile)
            self.rollback = "Database '{}' connected successfully.".format(self.name)
        except Exception as err:
            log_msg.error(err)
            self.rollback = "Something went wrong : {err}".format(err=err)


    def query(self, sql="", value = ""):
        try:
            self.con = self.conn.cursor()
            if sql !="" and value != "":
                self.con.execute(str(sql), value)
            else:
                self.con.execute(str(sql))
        except Exception as err:
            log_msg.error(err)
            self.rollback = err        
        return self

    def querymultiple(self, sql="", value = ""):
        try:
            self.con = self.conn.cursor()
            if sql !="" and value != "":
                self.con.executemany(str(sql), value)
            else:
                self.con.executemany(str(sql))
        except Exception as err:
            log_msg.error(err)
            self.rollback = err   
        return self


    def insert_id(self):
        return self.con.lastrowid

    def lastId(self):
        return self.con.lastrowid

    def fetch(self):
        result = self.con.fetchall()
        row = []
        for r in result:
            rowf = {}
            for idx, col in enumerate(self.con.description):
                rowf[col[0]] = r[idx]
            row.append(rowf)
        return row

    def queryone(self, sql="", value = ""):
        self.con = self.conn.cursor()
        if sql !="" and value != "":
            self.con.execute(str(sql), value)
        else:
            self.con.execute(str(sql))

        return self.con

    def all(self):
        self.result = self.fetch()
        return self.result

    def one(self):
        result = self.con.fetchone()
        row = {}
        for idx, col in enumerate(self.con.description):
            
            row[col[0]] = result[idx]
        return row

    def count(self):
        return self.con.rowcount

    def countall(self):
        self.all()
        return self.con.rowcount if self.con.rowcount > 0 else 0
     
    def save(self):
        try:
            self.conn.commit()
            return True
        except Exception as err:
            self.rollback = err
            log_msg.error(err)

    def close(self):
        return self.con.close()


    def create(self, TABLES = ''):
        self.con = self.conn.cursor()
        if TABLES:
            for table_name in TABLES:
                table_description = TABLES[table_name]
                try:
                    self.con.execute(table_description)
                    self.rollback = "Database table '{}' created successfully.".format(table_name)
                except Exception as err:
                
                    log_msg.info("Database table '{}' already exists.".format(table_name))
                    self.rollback =  "Database table '{}' already exists.".format(table_name)
            
            return self
        
        else:
            return False

