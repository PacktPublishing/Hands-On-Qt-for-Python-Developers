# -*- coding: utf-8 -*-         #   PYTHON 2   #
import pickle                                  # Import pickle stdlib module.
import shelve                                  # Import shelve stdlib module.
import csv                                     # Import csv stdlib module.
import os                                      # Import os stdlib module.
import pandas                                  # Pandas third-party package.
import sqlite3                                 # Import sqlite3 stdlib.
import psycopg2                                # PostgreSQL third-party.
import pymysql                                 # MySQL third-party package.
import pymongo                                 # Mongo third-party package.
import couchdb                                 # Couch third-party package.
from PySide2 import QtSql                      # QtSql module of the PySide2.

pathf = os.path.dirname(os.path.abspath(__file__))


class UTools(object):                          # Class for some functionality.

    def __init__(self):                        # Constructor of the class.
        self.us1 = "Application with Python."  # String variable.
        self.qtsql_db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.qtsql_db.setDatabaseName("data/u_db.sqlite")
        self.qtsql_db.open()                   # Path to DB. Open/Create DB.

    def pickle_dump(self, obj=None, filename=None, proto=1, fimps=None):
        fobj = open(filename, 'wb')            # File object in binary mode.
        if fimps is not None:                  # The fix_imports parameter.
            pickle.dump(obj, fobj, proto, fimps)
        else:                                  # Maps the new Python3 names,
            pickle.dump(obj, fobj)             # Python2 old module names,
        fobj.close()                           # not used with Python2.

    def pickle_load(self, filename=None, fimps=None, enc="ASCII", err="strict"):
        fobj = open(filename, 'rb')            # Loads the file with data, 
        if fimps is not None:                  # fix_imports is not None,
            pl = pickle.load(fobj, fimps, encoding=enc, errors=err)
        else:                                  # parameters for Python3,
            pl = pickle.load(fobj)             # defaults for Python3.
        fobj.close()                           # Used for Python2.
        return pl                              # Returns loaded data.

    def shelve_open(self, filename=None, flag='c', proto=None, writeback=False):
        return shelve.open(filename, flag, proto, writeback)

    def csv_write(self, csvfile=None, fieldnames=None, mode='a', newline='',
                  rowdata=None, dialect=csv.excel, delimiter=' ', quotechar='|',
                  lineterminator='\r\n'):      # Function to write CSV.
        csvpath = os.path.exists(r"%s/%s" % (pathf, csvfile))
        csvf = open(csvfile, mode)             # Opens file in append mode.  
        csvw = csv.DictWriter(csvf, fieldnames=fieldnames, dialect=dialect,
                              delimiter=delimiter, lineterminator=lineterminator)
        if csvpath is False:                   # If path of the file with
            csvw.writeheader()                 # writer exist - add header.
        csvdict = {k: v for (k, v) in zip(fieldnames, rowdata)}
        csvw.writerow(csvdict)                 # Writing row with dictionary.

    def csv_read(self, csvfile=None, mode='r', dialect=csv.excel):
        csvf = open(csvfile, mode)             # Opens file object (reading).
        csvr = csv.DictReader(csvf, dialect=dialect, delimiter=' ')
        return csvr                            # CSV dict reader object.

    def pandas_write(self, filename=None, writer="csv", data=None,
                     columns=None, index=None, dtype=object):
        df = pandas.DataFrame(data, columns=columns, index=index, dtype=dtype)
        df.index.name = "rows\columns"         # Function to write the pandas
        if writer == "csv":                    # csv, excel, etc., specified 
            df.to_csv(filename)                # in the writer parameter. 
        if writer == "excel":                  # Statements checks the type
            df.to_excel(filename)              # of file to write with pandas 
        if writer == "html":                   # functions. The data is dict
            df.to_html(filename)               # with keys - columns, values
        if writer == "json":                   # for this keys, indexes - the
            df.to_json(filename)               # number of rows. Returns
        return (df, writer)                    # data frame and writer.

    def pandas_read(self, filename=None, reader="csv", sep=',', delimiter=None,
                    engine='python', maxrows=999):
        if reader == "csv":                    # Reads file specified with
            df = pandas.read_csv(filename, engine=engine)
        if reader == "excel":                  # type of file with pandas.
            df = pandas.read_excel(filename)   # CSV file data, excel file
        if reader == "html":                   # data, html file data with
            df = pandas.read_html(filename)    # tags and used as html page,
        if reader == "json":                   # json representation etc.
            df = pandas.read_json(filename)    # Also, sets the options. 
        pandas.options.display.max_rows = maxrows
        return (df, reader)                    # Returns data and reader.

    def sqlite_insert(self, username=None, email=None, passw=None, data=None):
        dbcon = sqlite3.connect("%s/data/u_db.sqlite" % pathf)
        dbcursor = dbcon.cursor()              # Connect to the database.
        sql_query = """INSERT INTO u_dbtable (user_name, user_email,
                        user_passw, user_data) VALUES (?, ?, ?, ?);"""
        udata = (str(username), str(email), str(passw), str(data))
        dbcursor.execute(sql_query, udata)     # Executes the SQL query that   
        dbcon.commit()                         # SQL text, retreived data,
        dbcursor.close()                       # commit transaction then
        dbcon.close()                          # closes cursor and database.

    def sqlite_select(self):                   # Connect to the SQLite DB
        dbcon = sqlite3.connect("%s/data/u_db.sqlite" % pathf)
        dbcursor = dbcon.cursor()              # and open db cursor.
        sql_query = """SELECT info_date, user_name, user_email, user_passw,
                      user_data FROM u_dbtable;"""
        dbcursor.execute(sql_query)            # Executes the SQL query
        dbdata = dbcursor.fetchall()           # specified in the parameter,
        dbcursor.close()                       # fetch all data selected,
        dbcon.close()                          # closes cursor and database.
        return dbdata                          # Returns fetched data.

    def psql_insert(self, username=None, email=None, passw=None, data=None):
        dbcon = psycopg2.connect(dbname="psqldb")
        dbcursor = dbcon.cursor()              # Connects to the PostgreSQL.
        sql_query = """INSERT INTO u_dbtable (user_name, user_email,
                        user_passw, user_data) VALUES (%s, %s, %s, %s);""" 
        udata = (str(username), str(email), str(passw), str(data))
        dbcursor.execute(sql_query, udata)     # Executes the SQL query that    
        dbcon.commit()                         # specified in the parameter,
        dbcursor.close()                       # commit transaction then
        dbcon.close()                          # closes cursor and database.

    def psql_select(self):                     # Connect to the PostgreSQL
        dbcon = psycopg2.connect(dbname="psqldb")  
        dbcursor = dbcon.cursor()              # database and open db cursor.
        sql_query = """SELECT info_date, user_name, user_email, user_passw,
                       user_data FROM u_dbtable;"""
        dbcursor.execute(sql_query)            # Executes the SQL query that
        dbdata = dbcursor.fetchall()           # specified in the parameter
        dbcursor.close()                       # fetch all data selected,
        dbcon.close()                          # closes cursor and database.
        return dbdata                          # Returns fetched data.

    def mysql_insert(self, username=None, email=None, passw=None, data=None):
        dbcon = pymysql.connect(host="localhost", user="root",
                                password="rootpassword", db="mysqldb")
        dbcursor = dbcon.cursor()              # Connects to MySQL database.
        sql_query = """INSERT INTO u_dbtable (user_name, user_email,
                        user_passw, user_data) VALUES (%s, %s, %s, %s);"""
        udata = (str(username), str(email), str(passw), str(data))
        dbcursor.execute(sql_query, udata)     # Executes the SQL query that     
        dbcon.commit()                         # specified in the parameter.
        dbcursor.close()                       # commit transaction then
        dbcon.close()                          # closes cursor and database.

    def mysql_select(self):                    # Connects to MySQL database.
        dbcon = pymysql.connect(host="localhost", user="root",
								password="rootpassword", db="mysqldb")
        dbcursor = dbcon.cursor()              # Values with open db cursor.
        sql_query = """SELECT info_date, user_name, user_email, user_passw,
                       user_data FROM u_dbtable;"""
        dbcursor.execute(sql_query)            # Executes the SQL query that
        dbdata = dbcursor.fetchall()           # specified in the parameter
        dbcursor.close()                       # fetch all data selected,
        dbcon.close()                          # closes cursor and database.
        return dbdata                          # Returns fetched data.

    def sql_qt_insert(self, username=None, email=None, passw=None, data=None):
        query = QtSql.QSqlQuery(self.qtsql_db)
        query.prepare("""INSERT INTO u_dbtable (user_name, user_email,
                      user_passw, user_data) VALUES (:user_name, :user_email,
                     :user_passw, :user_data);""")
        query.bindValue(":user_name", username)
        query.bindValue(":user_email", email)
        query.bindValue(":user_passw", passw)  # Inserts values to the sqlite 
        query.bindValue(":user_data", data)    # database with QtSql module.
        query.exec_()                          # Executes the query to DB.

    def sql_qt_select(self):                   # Function for selection
        query = QtSql.QSqlQuery(self.qtsql_db)
        query.exec_("""SELECT * FROM u_dbtable;""")
        return query                           # values, QtSql module query.

    def mongo_insert(self, username=None, email=None, passw=None, data=None):
        client = pymongo.MongoClient('localhost', 27017)
        db = client['umongodb']                # Connection to the MongoDB. 
        post = {"User Name": username, "Email": email,
                "Password": passw, "Data": data}
        posts = db.posts                       # Creating the dictionary and
        posts.insert_one(post)                 # inserting with name posts.

    def mongo_select(self):                    # Selection from MongoDB.
        client = pymongo.MongoClient('localhost', 27017)
        db = client['umongodb']                # Connection to the DB with
        dbdata = db.posts.find()               # client and find in the posts
        return dbdata                          # collections this data.

    def couch_insert(self, username=None, email=None, passw=None, data=None):
        couch = couchdb.Server("http://127.0.0.1:5984/")
        db = couch["u_couchdb"]                # Connection to the CouchDB. 
        dbdata = {"User Name": username, "User email": email,
                  "User password": passw, "User Data": data}
        db.save(dbdata)                        # Saving data to the database.
                  
    def couch_select(self):                    # Selection from CouchDB.
        couch = couchdb.Server("http://127.0.0.1:5984/")  # 
        db = couch["u_couchdb"]                # Connection to the server,
        return db                              # returns of the documents.


if __name__ == "__main__":                     # Instruction when run file.
    ut = UTools()                              # Class instance, will run.
