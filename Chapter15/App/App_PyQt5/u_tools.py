# -*- coding: utf-8 -*-         #   PYTHON 3   #
import os                                      # Import os stdlib module.
import time                                    # Import time stdlib module.
import pickle                                  # Import pickle stdlib module.
import shelve                                  # Import shelve stdlib module.
import csv                                     # Import csv stdlib module.
import sqlite3                                 # Import sqlite3 stdlib.
import psycopg2                                # PostgreSQL third-party.
import pymysql                                 # MySQL third-party package.
import pymongo                                 # Mongo third-party package.
import couchdb                                 # Couch third-party package.
from PyQt5 import QtSql                        # QtSql module of the PyQt5.
from PyQt5.QtCore import pyqtSignal as app_signal
from PyQt5.QtCore import pyqtSlot as app_slot  # Importing slots of PyQt5.
from PyQt5.QtCore import QThread               # Importing for threads.

pathf = os.path.dirname(os.path.abspath(__file__))


class WPandas(QThread):                        # Thread for writing file with

    sig1 = app_signal(object, str)             # Pandas. Signal for emitting

    def __init__(self, parent=None):           # from this thread. Will write
        super(WPandas, self).__init__(parent)  # the pandas csv, excel,

    def on_source(self, datas):                # specified in the writer
        self.datas = datas                     # parameter. The 'if'

    def run(self):                             # statements checks the type
        try:                                   # of file to write with using
            import pandas                      # pandas functions. List of
            uindex = [i for i in range(self.datas[2])]
            udata = {"User_Name": range(0, self.datas[2]),
                     "User_email": range(0, self.datas[2]),
                     "User_password": range(0, self.datas[2]),
                     "User_data": range(0, self.datas[2])}
            df = pandas.DataFrame(udata, columns=self.datas[3], index=uindex,
                                  dtype=self.datas[5])
            df.index.name = "rows\columns"     # indexes. The data is a dict
            if self.datas[1] == "csv":         # with specified keys and   
                df.to_csv(self.datas[0])       # columns, value pairs of
            if self.datas[1] == "excel":       # these keys, The index list
                df.to_excel(self.datas[0])     # is the number of rows. Data
            if self.datas[1] == "html":        # can be written to the excel,  
                df.to_html(self.datas[0])      # html, json files also. The  
            if self.datas[1] == "json":        # user data can be changed
                df.to_json(self.datas[0])      # to the real world data. Then
            if self.isFinished():              # checks if this thread is
                self.quit()                    # finished and quits thread. 
        except Exception as err:               # If some error will occur -
            self.sig1.emit('', str(err))       # emits this error to app, 
            if self.isFinished():              # checks, if the thread is
                self.quit()                    # finished, quits this thread.


class RPandas(QThread):                        # Thread for reading CSV file

    sig1 = app_signal(object, str)             # with Pandas. Emits an object

    def __init__(self, parent=None):           # (dataframe). Will read the
        super(RPandas, self).__init__(parent)  # file that specified with

    def on_source(self, datas):                # type of the file with an
        self.datas = datas                     # representation to the pandas

    def run(self):                             # dataframe that can be opened
        try:                                   # as csv file data, excel file
            import pandas                      # data, html file data with   
            if self.datas[1] == "csv":         # tags and can be used as html   
                df = pandas.read_csv(self.datas[0], chunksize=self.datas[6],
                                     engine=self.datas[4]) 
            if self.datas[1] == "excel":       # page, json representation.  
                df = pandas.read_excel(self.datas[0])    
            if self.datas[1] == "html":        # Also, sets the options to 
                df = pandas.read_html(self.datas[0])
            if self.datas[1]== "json":         # display number of rows.
                df = pandas.read_json(self.datas[0])   
            pandas.options.display.max_rows = self.datas[5]
            for ch in df:                      # Returns data and reader that
                self.sig1.emit(ch, '')         # used as chunk sizes to split
                time.sleep(0.1)                # reading of the file data.
            if self.isFinished():              # checks if this thread is
                self.quit()                    # finished and quits thread. 
        except Exception as err:               # If some error will occur -
            self.sig1.emit('', str(err))       # emits this error to app, 
            if self.isFinished():              # checks, if the thread is
                self.quit()                    # finished, quits this thread.


class UTools(object):                          # Class forsome functionality.
    
    pandas_sig1 = app_signal(list)             # Signal for pandas writing.
    pandas_sig2 = app_signal(list)             # Signal for pandas reading.
    
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
        data = 1000000                         # Function will write data
        index = 1000000                        # with Pandas. Integers are
        datas = [filename, writer, data, columns, index, dtype]
        self.pandas_thread1 = WPandas()        # used to generate values for
        self.pandas_sig1.connect(self.pandas_thread1.on_source)
        self.pandas_sig1.emit(datas)           # each cell of the CSV file,
        self.pandas_thread1.start()            # using thread, 1000000 rows.

    def pandas_read(self, filename=None, reader="csv", sep=',', delimiter=None,
                    engine='python', maxrows=9, chunk=10000):
        datas = [filename, reader, sep, delimiter, engine, maxrows, chunk]
        self.pandas_thread2 = RPandas()        # Function reads the data
        self.pandas_sig2.connect(self.pandas_thread2.on_source)
        self.pandas_sig2.emit(datas)           # from the CSV file with
        self.pandas_thread2.start()            # Pandas using thread which
        return self.pandas_thread2             # returned for operating.

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