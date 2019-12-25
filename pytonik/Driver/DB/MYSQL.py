###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
###

from pytonik import Log
log_msg = Log.Log()

try:
    import mysql.connector
except Exception as err:
    log_msg.critical(err)


class MYSQL:

    def __init__(self, setting):
        self.settings = setting
        self.host = setting['host']
        self.database = setting['database']
        self.username = setting['username']
        self.password = setting['password']
        self.prefix = setting['prefix']
        self.Exception = ""
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
        except mysql.connector.Error as err:
            log_msg.error(err)
            self.Exception = "Something went wrong : {err}".format(err=err)


    def query(self, sql="", value = ""):
        try:
            self.con = self.conn.cursor(dictionary=True)
            if sql !="" and value != "":
                self.con.execute(str(sql), value)
            else:
                self.con.execute(str(sql))
        except Exception as err:
            log_msg.error(err)
            self.Exception = err
              
        return self

    def querymultiple(self, sql="", value = ""):
        try:
            self.con = self.conn.cursor(dictionary=True)
            
            if sql !="" and value != "":
                self.con.executemany(str(sql), value)
            else:
                self.con.executemany(str(sql))
        except Exception as err:
            log_msg.error(err)
            self.Exception = err
            
        return self


    def insert_id(self):
        return self.con.lastrowid

    def lastId(self):
        return self.con.lastrowid

    def fetch(self):
            return self.con.fetchall()

    def queryone(self, sql="", value = ""):
        self.con = self.conn.cursor(buffered=True)
        if sql !="" and value != "":
            self.con.execute(str(sql), value)
        else:
            self.con.execute(str(sql))

        return self.con

    def all(self):
        self.result = self.fetch()
        return self.result

    def one(self):
        return self.con.fetchone()

    def count(self):
        return self.con.rowcount

    def countall(self):
        self.all()
        return self.con.rowcount

    def save(self):
        try:
            self.conn.commit()
            return True
        except Exception as err:
            self.Exception = err
            log_msg.error(err)
            return self

    def close(self):
        return self.con.close()

    def create(self, TABLES = ''):
        self.con = self.conn.cursor()
        if TABLES:
            for table_name in TABLES:
                table_description = TABLES[table_name]
                try:
                    self.con.execute(table_description)
                except mysql.connector.Error as err:
                        log_msg.info("Database table '{}' already exists.".format(table_name))
                        self.Exception =  "Database table '{}' already exists.".format(table_name)
            return self          
        else:
            return False
