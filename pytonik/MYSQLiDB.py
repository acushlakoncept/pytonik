###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###

from . import Log
log_msg = Log.Log()

try:
    import mysql.connector
except Exception as err:
    log_msg.critical(err)


class MYSQLiDB:
    global connect, con
    def __init__(self, setting):
        self.settings = setting
        self.host = setting['host']
        self.database = setting['database']
        self.username = setting['username']
        self.password = setting['password']
        self.conn =  None
        self.con = None
        self.result = None
        self.connectDB()

    def connectDB(self):

        try:

            self.conn = mysql.connector.connect(
                    host=self.host,
                    user=self.username,
                    passwd=self.password,
                    database=self.database
            )
            self.con = self.conn.cursor(dictionary=True)

        except mysql.connector.Error as err:
            log_msg.error(err)
            return ("Something went wrong : {err}".format(err=err))


    def query(self, sql="", value = ""):

        if sql !="" and value != "":
            self.con.execute(str(sql), value)
        else:
            self.con.execute(str(sql))
            #self.result = self.con.fetchall()
            #self.fetch()
        return self.con


    def insert_id(self):
        return self.con.lastrowid

    def lastId(self):
        return self.con.lastrowid

    def fetch(self):
        import json

        if self.result != "" and self.result is not None:
            return self.result
        else:
            return False

    global dictv
    dictv = dict()
    def addDict(self, k, v):

        for i in dictv:
            if i == k:
                print(i)
                print('error')
                return
        #dictv[k] = v

    def all(self):
        self.result = self.con.fetchall()
        return  self.fetch()

    def one(self):
        return self.con.fetchone()

    def countrow(self):
        return self.con.rowcount

    def countall(self):
        self.all()
        return self.con.rowcount

    def save(self):
        try:
            self.conn.commit()
            return True
        except Exception as err:
            return err

    def close(self):
        return self.con.close()

