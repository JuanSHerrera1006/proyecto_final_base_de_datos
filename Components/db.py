import pandas as pd
import os
import sqlite3
import traceback
import datetime as dt


def create_db(db_name,db_path):

  try:
      # Create connection to sqlite3
      conn = sqlite3.connect(os.path.join(db_path,db_name))
      cursor = conn.cursor()
      # Creation of tables
      cursor.execute("""CREATE TABLE IF NOT EXISTS Dim_Fecha(
          fecha TIMESTAMP PRIMARY KEY,
          year INTEGER,
          month INTEGER,
          day INTEGER)""")
      cursor.execute("""CREATE TABLE IF NOT EXISTS Dim_Integrante(
          id_integrante INTEGER PRIMARY KEY AUTOINCREMENT,
          descripcion_integrante TEXT)""")
      cursor.execute("""CREATE TABLE IF NOT EXISTS Fct_Gastos(
          id_gasto INTEGER PRIMARY KEY AUTOINCREMENT,
          fecha TEXT,
          id_integrante INTEGER,
          flujo_casa_mes TEXT,
          valor INTEGER,
          forma_de_pago TEXT,
          nombre_categoria TEXT,
          FOREIGN KEY (id_integrante) REFERENCES Dim_Integrante(id_integrante),
          FOREIGN KEY (fecha) REFERENCES Dim_Fecha(fecha))""")
      cursor.execute("""CREATE TABLE IF NOT EXISTS Fct_Ingresos(
          id_ingreso INTEGER PRIMARY KEY AUTOINCREMENT,
          fecha TEXT,
          id_integrante INTEGER,
          flujo_casa_mes TEXT,
          valor INTEGER,
          forma_de_pago TEXT,
          nombre_categoria TEXT,
          FOREIGN KEY (id_integrante) REFERENCES Dim_Integrante(id_integrante),
          FOREIGN KEY (fecha) REFERENCES Dim_Fecha(fecha))""")
      # Close connection
      conn.commit()
      conn.close()
  except Exception as e:
      print('Error: ',e )
      print(traceback.format_exc())
  return None
