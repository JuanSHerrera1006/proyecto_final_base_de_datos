import pandas as pd
import os
import sqlite3
import traceback
import datetime as dt

def insert_data(df_file,db_name,db_path,i):
    try:
        if os.path.exists(os.path.join(db_path, db_name)):
            # Check if the tables of the data warehouse are not empty
            conn = sqlite3.connect(os.path.join(db_path, db_name))
            cursor = conn.cursor()
            # Close connection
            conn.commit()
            conn.close()
    except Exception as e:
        print('Error: ',e)
        print(traceback.format_exc())
    return None