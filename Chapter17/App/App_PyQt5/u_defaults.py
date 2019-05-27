# -*- coding: utf-8 -*-         #   PYTHON 3   #
import os                                      # Imports stdlib os module.
import sqlite3                                 # Importing SQLite database.

dbpath = os.path.dirname(os.path.abspath(__file__))


def txt_file(state=False):                     # Writes default colors.
    colors = "rgba(0,41,59,140) rgba(0,41,59,255) rgba(1,255,217,140) rgba(1,255,217,255)"
    if os.path.exists("settings.txt") is state:
        wstyle = open("settings.txt", "w")     # If the file does not exist,
        wstyle.write(colors)                   # creates default file, writes
        wstyle.close()                         # the colors. Close object.


dbcon = sqlite3.connect("%s/data/u_db.sqlite" % dbpath)
dbcursor = dbcon.cursor()                      # Connects database with path.
sql_query = """CREATE TABLE IF NOT EXISTS u_dbtable (
                info_date DEFAULT CURRENT_TIMESTAMP, user_name TEXT UNIQUE,
                user_email TEXT UNIQUE, user_passw TEXT, user_data TEXT UNIQUE);"""
dbcursor.execute(sql_query)                    # Executes the SQL query that 
dbcursor.close()                               # specified in the parameter,
dbcon.close()                                  # closes cursor and database.
