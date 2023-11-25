import pandas as pd
import os
import sqlite3
import traceback
import datetime as dt
from constants import constants


def create_db(db_name,db_path):
  try:
      # Create connection to sqlite3
      conn = sqlite3.connect(os.path.join(db_path,db_name))
      cursor = conn.cursor()
      # Creation of tables
      cursor.execute(constants.QUERY_TABLE_TIPO_TIENDA)
      cursor.execute(constants.QUERY_TABLE_BARRIO)
      cursor.execute(constants.QUERY_TABLE_TIPO_DOCUMENTO)
      cursor.execute(constants.QUERY_TABLE_CLIENTE)
      cursor.execute(constants.QUERY_TABLE_TIENDA)
      cursor.execute(constants.QUERY_TABLE_COMPRA)
      # Close connection
      conn.commit()
      conn.close()
  except Exception as e:
      print('Error: ',e )
      print(traceback.format_exc())
  return None
