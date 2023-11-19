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
            if pd.read_sql("""SELECT * FROM Fct_Gastos""", conn).empty:

                # Dim_Integrante
                integrantes = ['madre', 'padre', 'hijo']
                for integrante in integrantes:
                  cursor.execute('''INSERT INTO Dim_Integrante (descripcion_integrante) VALUES (?)''', (integrante,))


                # Dim_Fecha
                df_dim_fecha = df_file[['fecha']].drop_duplicates()

                df_dim_fecha['year'] = df_dim_fecha['fecha'].apply(lambda x: x.year)
                df_dim_fecha['month'] = df_dim_fecha['fecha'].apply(lambda x: x.month)
                df_dim_fecha['day'] = df_dim_fecha['fecha'].apply(lambda x: x.day)

                df_dim_fecha = df_dim_fecha.sort_values(by=['fecha'])

                for index, row in df_dim_fecha.iterrows():
                  fecha_str = row['fecha'].strftime('%Y-%m-%d %H:%M:%S')
                  cursor.execute("INSERT INTO Dim_Fecha (fecha, year, month, day) VALUES (?, ?, ?, ?)", (fecha_str, row['year'], row['month'], row['day']))


                # Fct_Gastos
                df_dim_gastos = df_file.loc[~df_file['flujo_casa_mes'].str.contains('contrato', case=False, na=False)]
                df_dim_gastos = df_dim_gastos.sort_values(by=['fecha'])
                for index, row in df_dim_gastos.iterrows():
                    fecha_str = row['fecha'].strftime('%Y-%m-%d %H:%M:%S')
                    cursor.execute("INSERT INTO Fct_Gastos (fecha,flujo_casa_mes,valor,forma_de_pago,nombre_categoria,id_integrante) VALUES (?,?,?,?,?,?)", (fecha_str,row['flujo_casa_mes'],row['valor'],row['forma_de_pago'],row['nombre_categoria'],i))

                # Fct_Ingresos
                df_dim_ingresos = df_file.loc[df_file['flujo_casa_mes'].str.contains('contrato', case=False, na=False)]
                df_dim_ingresos = df_dim_ingresos.sort_values(by=['fecha'])

                for index, row in df_dim_ingresos.iterrows():
                    fecha_str = row['fecha'].strftime('%Y-%m-%d %H:%M:%S')
                    cursor.execute("INSERT INTO Fct_Ingresos (fecha,flujo_casa_mes,valor,forma_de_pago,nombre_categoria,id_integrante) VALUES (?,?,?,?,?,?)", (fecha_str,row['flujo_casa_mes'],row['valor'],row['forma_de_pago'],row['nombre_categoria'],i))


                # Close connection
                conn.commit()
                conn.close()
    except Exception as e:
        print('Error: ',e)
        print(traceback.format_exc())
    return None