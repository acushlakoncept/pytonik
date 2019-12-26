###
# Author : Betacodings
# Author : info@betacodings.com
# Maintainer By: Emmanuel Martins
# Maintainer Email: emmamartinscm@gmail.com
# Created by Betacodings on 2019.
#############################################
#############################################
# Support Table Artisan Conducts Database querys
# Using Schema Pattern to controller callable funtions and methods
# Each method represent query builder attribute

    
from pytonik  import App, Version, Log

app = App.App()

class Table:
    
    def __init__(self, table=""):
        self.DB = app.DB()
        self.prefix = self.DB.prefix 
        self.table = str(self.prefix)+str(table)
        self.tabledict = table
        self.result = None
        self.rowCount = None
        self.table_select = ""
        self.table_exist = ""
        self.table_notexist =  ""
        self.table_where = ""
        self.table_drop = ""
        self.table_delete  = ""
        self.table_value  = ""
        self.table_pluck  = ""
        self.table_groupby  = ""
        self.table_orderby  = ""
        self.table_offset  = ""
        self.table_limit  = ""
        self.table_join   = ""
        self.table_leftjoin   = ""
        self.table_rightjoin   = ""
        self.table_max   = ""
        self.table_min   = ""
        self.table_count   = ""
        self.table_distinct   = ""
        self.table_avg   = ""
        self.error = ""
        return None
   
    def drop(self):
        self.table_drop = "DROP TABLE {exists} {table}".format(table = self.table, exists='IF '+ str(self.table_exist) if self.table_exist is not "" else "")
        t_result = self.DB.query(self.table_drop)
        self.error = t_result.Exception
        return self 
    
    def exists(self, rawquery=""):
        rawString = "WHERE EXISTS ({rawquery})".format(rawquery=rawquery) if rawquery is not "" else "EXISTS"
        self.table_exist =  "{rawquery}".format(rawquery = rawString)
        return self
    
    def notExist(self, rawquery=""):
        rawString =  "WHERE NOT EXISTS ({rawquery})".format(rawquery=rawquery) if rawquery is not "" else "NOT EXISTS"
        self.table_notexist =  "{rawquery}".format(rawquery = rawString)
        return self
  
    def select(self):
        self.table_select = "SELECT {distinct} {values} {pluck} {max} {min} {count} {avg} FROM {table} {exists} {notexist} {join} {leftjoin} {rightjoin} {where} {groupBy} {orderBy} {limit}".format(
            distinct = self.table_distinct, 
            values = self.table_value if self.table_value is not "" else '*', 
            pluck = self.table_pluck if self.table_pluck is not "" else '', 
            max = self.table_max,  
            min = self.table_min,  
            count = self.table_count,  
            avg = self.table_avg,  
            table = self.table,
            exists = self.table_exist,
            notexist =  self.table_notexist,  
            join=self.table_join, 
            leftjoin = self.table_leftjoin, rightjoin = self.table_rightjoin, 
            where = self.table_where, groupBy = self.table_groupby, 
            orderBy = self.table_orderby, limit = self.table_limit)
        
        t_result = self.DB.query(self.table_select)
        self.error = t_result.Exception
        return self
    
    def max(self, column):
        self.table_max = ", MAX({column})".format(column=column)
        return self
    
    def min(self, column):
        self.table_min = ", MIN({column})".format(column=column)
        return self
    
    def count(self, column="*"):
        self.table_count = ", COUNT({column})".format(column=column)
        return self
        
    def avg(self, column):
        self.table_avg = ", AVG({column})".format(column=column)
        return self  
    
    def distinct(self, column):
        self.table_distinct = "DISTINCT ".format(column=column)
        return self
    
    def where(self, variable, sign, string):
        string_type = "'{string}'".format(string=string) if (type(string) == str) == True else string
        self.table_where = "WHERE {variable} {sign} {string}".format(variable=variable, sign=sign, string=string_type)
        return self
    
    def whereNull(string):
        self.table_whereisnull = "WHERE {string} IS NULL".format(string=string)
        return self
        
    def delete(self):
        self.table_delete = "DELETE FROM {table} {where}".format(table = self.table, where = self.table_where)
        t_result = self.DB.query(self.table_delete)
        return t_result.save() if t_result.Exception == "" else t_result.Exception
    
    
    def groupBy(self, *values):
        self.table_groupby = "GROUP BY {values}".format(values = ' , '.join(values))
        return self
    
    
    def orderBy(self, value, sort):
        self.table_orderby = "ORDER BY {value} {sort}".format(value = value, sort=sort)
        return self
    
    def offset(self, offset=""):
        self.table_offset =  str(offset) + ',' if offset is not "" else 0
        return self
    
    def limit(self, limits):
        
        self.table_limit = "LIMIT {offset} {limit}".format(offset = self.table_offset, limit=limits)
        return self
    
    def value(self, *values):
        self.table_value = "{values}".format(values = ' , '.join(values))
        return self

    def join(self, table, variable, sign, string):

        self.table_join = "JOIN {table} ON {variable} {sign} {string}".format(table=str(self.prefix)+str(table), variable = variable, sign=sign, string=string)
        return self

    def leftJoin(self, table, variable, sign, string):

        self.table_leftjoin = "LEFT JOIN {table} ON {variable} {sign} {string}".format(table=str(self.prefix)+str(table), variable = variable, sign=sign, string=string)
        return self

    def rightJoin(self, table, variable, sign, string):
        self.table_rightjoin = "RIGHT JOIN {table} ON {variable} {sign} {string}".format(table=str(self.prefix)+str(table), variable = variable, sign=sign, string=string)
        return self

    
    def pluck(self, *column):
        self.table_pluck = ", {column}".format(column =' AS '.join(column))
        return self
    
    
    def find(self, num=0):
        self.table_find = "SELECT * FROM {table} ".format(table=str(self.prefix)+str(self.table))
        t_result = self.DB.query(self.table_find)
        r = ""
        if t_result.Exception == "":
            get = self.get()
            if get.rowCount > 0:
                rg = get.result
                for l in rg:
                    rf = {}
                    if Version.PYVERSION_MA <= 2:
                        lt = l.iteritems()
                    else:
                        lt = l.items()
                    for k, v in lt:
                        lk = l[k]
                        if lk == num:
                            r=l
            else:        
                r = ""
        else:
            r = t_result.Exception
            
        return r
        
    def update(self, data=[]):
        if (type(data) == list):
            if len(data) > 0:
                value = []
                column = []
                for l in data:
                    value.append(l) 
                    if Version.PYVERSION_MA <= 2:
                        lt = l.iteritems()
                    else:
                        lt = l.items()
                    for k, v in lt: 
                        if k not in column:
                            column.append( '{k}="{v}"'.format(k=k, v=v))
                        
                lcolumn = ' , '.join(column)
                
                table_update ="UPDATE {table} SET {column} {where}".format(table=str(self.prefix)+str(self.table),  column=lcolumn, where=self.table_where)
                t_result = self.DB.query(table_update)
                return t_result.save() if t_result.Exception == "" else t_result.Exception
            else:
                return "Empty Data"
        else:
            return "Only Accepts type list"
        
        
    def insert(self, data=[]):
        if (type(data) == list):
            if len(data) > 0:
                ksys = []
                value = []
                val = []
                column = []
                il = 1
                for l in data:
                    value.append(l) 
                    if Version.PYVERSION_MA <= 2:
                        lt = l.iteritems()
                    else:
                        lt = l.items()
                    il +=1
                    ksys.append(':{}'.format(il))
                    for k, v in lt: 
                        if k not in column:
                            column.append(k)        
                    val.append(tuple(l.values()))
                          
                lcolumn = ' , '.join(column)
                kvariables = ' ,'.join(ksys)
 
                
               
                table_insert = "INSERT INTO  {table}  ({column}) VALUES ({kvariables}) ".format(table=str(self.prefix)+str(self.table), column=lcolumn, kvariables=kvariables)
                
                if len(value) == 1:
                    t_result = self.DB.query(table_insert , val[0])
                else:
                    t_result = self.DB.querymultiple(table_insert, val)
                return t_result.save() if t_result.Exception == "" else t_result.Exception
            else:
                return "Empty Data"
        else:
            return "Only Accepts type list"
    
    def create(self):
        if type(self.tabledict) == dict:
            for table_name in self.tabledict:
                table_description = self.tabledict[table_name]
                t_result = self.DB.query(table_description)
            return t_result.save() if t_result.Exception == "" else t_result.Exception
        else:
            return "Accepts type dictionary"
    
    def raw(self, rawstring):
        return rawstring
    
    def get(self):
        self.result = self.DB.fetch()
        self.rowCount = self.DB.count()
        return self
               
    
        
        