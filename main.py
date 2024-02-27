import sqlite3
import pandas as pd
import os
import glob
import pathlib

def main():
    connect_to_sqlite_db()
    csv_to_db()

def connect_to_sqlite_db():
    #Create a database connection and cursor to execute queries.
    global conn, c
    conn = sqlite3.connect('my_data.db')
    c = conn.cursor()

def csv_to_db():
    #Read all csv files in /csv directory 
    path = os.getcwd() + "/csv"
    csv_files = glob.glob(os.path.join(path, "*.csv"))
    #Create/update table according to csv name and headers and load data to db.
    for f in csv_files:
        #Takes file name without extension
        table_name = pathlib.Path(f).stem
        #Inserts csv data to db
        data_frames = pd.read_csv(f, header=0, sep=',')
        data_frames.to_sql(table_name, conn, if_exists='append', index = False)

main()