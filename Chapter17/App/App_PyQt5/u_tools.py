# -*- coding: utf-8 -*-         #   PYTHON 3   #
import os                                      # Import os stdlib module.
import time                                    # Import time stdlib module.
import pickle                                  # Import pickle stdlib module.
import shelve                                  # Import shelve stdlib module.
import csv                                     # Import csv stdlib module.
import sqlite3                                 # Import sqlite3 stdlib.
import psycopg2                                # PostgreSQL third-party.
import pymysql                                 # MySQL third-party package.
from PyQt5 import QtSql                        # QtSql module of the PyQt5.
from PyQt5.QtCore import pyqtSignal as app_signal
from PyQt5.QtCore import pyqtSlot as app_slot  # Importing slots of PyQt5.
from PyQt5.QtCore import QThread, QObject, QMutex

pathf = os.path.dirname(os.path.abspath(__file__))


class RunThread(QObject):                      # Class for running script

    sig1 = app_signal(object, object, str)     # with thread. Inherits

    def __init__(self, parent=None, datas=None):
        super(RunThread, self).__init__(parent)
        self.datas = datas                     # QObject class, retreives

    def on_run_code(self):                     # data for execution, and
        try:                                   # three types foremitting
            import subprocess                  # signals. Function, that will
            wf = open("temp.py", "w")          # run, imports subprocess,
            wf.write(self.datas)               # writes file with data that
            wf.close()                         # received, close file. Popen
            sp = subprocess.Popen(["python", "temp.py"], stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE)
            out = sp.communicate()             # class of the subprocess. For
            self.sig1.emit(out[0].decode("utf-8"), out[1].decode("utf-8"), '')
        except Exception as err:               # output data with using
            self.sig1.emit('', '', str(err))   # communicate() method.


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
            if self.isFinished():              # Checks, if the thread is
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
            if self.isFinished():              # Checks if this thread is
                self.quit()                    # finished and quits thread. 
        except Exception as err:               # If some error will occur -
            self.sig1.emit('', str(err))       # emits this error to app, 
            if self.isFinished():              # checks, if the thread is
                self.quit()                    # finished, quits this thread.


class MongoThread(QThread):                    # Thread for access MongoDB.

    sig1 = app_signal(object, str)             # Signal emit with data/error.

    def __init__(self, parent=None):           # Importing of the pymongo
        super(MongoThread, self).__init__(parent)

    def on_source(self, datas):                # adapter for connection.
        self.datas = datas                     # Receives the data as

    def run(self):                             # dictionary and inserting to
        try:                                   # the mongo database. The
            import pymongo                     # datas received contains
            try:                               # insert or select string that
                self.client = pymongo.MongoClient('localhost', 27017)
                self.db = self.client['umongodb']
            except pymongo.errors as err:      # used for which  operation
                self.sig1.emit('', str(err))   # need to do. If insert - this
            if self.datas[1] == "insert":      # data will be inserted to the
                posts = self.db.posts          # database. If the value of
                posts.insert_one(self.datas[0])
            if self.datas[1] == "select":      # datas is select - will find
                dbdata = self.db.posts.find()  # in the posts and emits this
                self.sig1.emit(dbdata, '')     # data or error if occured.
            if self.isFinished():              # Checks if this thread is
                self.quit()                    # finished and quits thread. 
        except Exception as err:               # If some error will occur -
            self.sig1.emit('', str(err))       # emits this error to app, 
            if self.isFinished():              # checks, if the thread is
                self.quit()                    # finished, quits this thread.


class CouchThread(QThread):                    # Thread for access CouchDB.

    sig1 = app_signal(object, str)             # Signal will emit data/error.

    def __init__(self, parent=None):           # Importing of the couchdb
        super(CouchThread, self).__init__(parent)

    def on_source(self, datas):                # adapter for connection. Then
        self.datas = datas                     # receives the data as a

    def run(self):                             # dictionary and inserting to
        try:                                   # the couch database. The
            import couchdb                     # datas received contains
            try:                               # insert or select string that
                self.couch = couchdb.Server("http://127.0.0.1:5984/")
                self.db = self.couch["u_couchdb"]
            except Exception as err:           # used for which operation
                self.sig1.emit('', str(err))   # need to do. If insert - this
            if self.datas[1] == "insert":      # data will be inserted to the
                self.db.save(self.datas[0])    # couch database If select
            if self.datas[1] == "select":      # value - emits the couchdb  
                self.sig1.emit(self.db, '')    # data or error if occurs.
            if self.isFinished():              # Checks if this thread is
                self.quit()                    # finished and quits thread. 
        except Exception as err:               # If some error will occur -
            self.sig1.emit('', str(err))       # emits this error to app, 
            if self.isFinished():              # checks, if the thread is
                self.quit()                    # finished, quits this thread.


class PaintThread(QThread):                    # Thread for draw operations.

    sig1 = app_signal(object, str)             # Signal will emit data/error.

    def __init__(self, parent=None):           # This thread can read the 
        super(PaintThread, self).__init__(parent)

    def on_source(self, datas):                # CSV files with data and try
        self.datas = datas                     # to visualize the results.

    def run(self):                             # Will be used pandas tool
        try:                                   # for read the CSV file with
            import pandas                      # chunck size specified. This
            df = pandas.read_csv("data/bigtests.csv", chunksize=1000,
                                 engine="python")
            r = self.datas[1]                  # simple demonstration will 
            h = self.datas[1] / 1000           # receive the width and height
            for ch in df:                      # and implemnent the data
                wx = self.datas[0] / 1000000   # on the graphics scene in 
                w = ch["User_Name"].values[777] * wx
                xy = (float(r), float(w))      # this relation. Then will 
                self.sig1.emit(xy, '')         # emit the tuple with position
                time.sleep(0.05)               # of the point that related to
                r -= h                         # data for line construction.
            if self.isFinished():              # The signals will be emmited
                self.quit()                    # with interval 0.05 seconds.
        except Exception as err:               # Are used just one value of
            self.sig1.emit('', str(err))       # the chunk and it can be
            if self.isFinished():              # changed in the relation to
                self.quit()                    # tasks of data visualization.


class UTools(object):                          # Class forsome functionality.

    pandas_sig1 = app_signal(list)             # Signal for pandas writing.
    pandas_sig2 = app_signal(list)             # Signal for pandas reading.
    mongo_sig1 = app_signal(list)              # Signals for communication
    mongo_sig2 = app_signal(list)              # with thread for MongoDB.
    couch_sig1 = app_signal(list)              # Signals for communication
    couch_sig2 = app_signal(list)              # with thread for CouchDB.
    paint_sig = app_signal(list)               # Signal for draws function.
    
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
        datas = [{"User Name": username, "Email": email, "Password": passw,
                  "Data": data}, "insert"]     # Inserting values to the
        self.mongo_thread1 = MongoThread()     # Mongo database using thread
        self.mongo_sig1.connect(self.mongo_thread1.on_source)
        self.mongo_sig1.emit(datas)            # and emitting of the data
        self.mongo_thread1.start()             # specified in the list.

    def mongo_select(self):                    # Selection values from
        datas = [{}, "select"]                 # MongoDB using thread
        self.mongo_thread2 = MongoThread()     # for reading. Sending to
        self.mongo_sig2.connect(self.mongo_thread2.on_source)
        self.mongo_sig2.emit(datas)            # thread the empty dict and
        self.mongo_thread2.start()             # and second select string,
        return self.mongo_thread2              # then returning thread.

    def couch_insert(self, username=None, email=None, passw=None, data=None): 
        datas = [{"User Name": username, "User email": email,
                 "User password": passw, "User Data": data}, "insert"]
        self.couch_thread1 = CouchThread()     # Function for writing
        self.couch_sig1.connect(self.couch_thread1.on_source)
        self.couch_sig1.emit(datas)            # to the Couch database with
        self.couch_thread1.start()             # data specified in the list.
                  
    def couch_select(self):                    # Selection values from
        datas = [{}, "select"]                 # CouchDB with using
        self.couch_thread2 = CouchThread()     # thread. Returns the
        self.couch_sig2.connect(self.couch_thread2.on_source)
        self.couch_sig2.emit(datas)            # database that will be
        self.couch_thread2.start()             # used to get the values
        return self.couch_thread2              # and insert to text field.

    def run_code(self, datas=None):            # Thread construction with
        self.run_thread = QThread()            # moveToThread() method of
        self.run_obj = RunThread(datas=datas)  # the QObject class. Thread
        self.run_obj.moveToThread(self.run_thread)
        self.run_thread.started.connect(self.run_obj.on_run_code)
        self.run_thread.start()                # created. Moves class to
        return (self.run_thread, self.run_obj) # thread, function for run.

    def draws(self, w=None, h=None):           # This function will be used
        datas = [w, h]                         # for manipulations and
        self.paint_thread = PaintThread()      # communication with thread
        self.paint_sig.connect(self.paint_thread.on_source)
        self.paint_sig.emit(datas)             # for draw the data to the 
        self.paint_thread.start()              # app. Will start the thread
        return self.paint_thread               # and return thread object.


if __name__ == "__main__":                     # Instruction when run file.
    ut = UTools()                              # Class instance, will run.
