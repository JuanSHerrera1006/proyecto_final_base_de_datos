from constants import constants
import pandas as pd
import os
import sqlite3
import traceback

def insert_data(df_file,db_name,db_path):
    try:
        if os.path.exists(os.path.join(db_path, db_name)):
            conn = sqlite3.connect(os.path.join(db_path, db_name))
            cursor = conn.cursor()
            
            if pd.read_sql('SELECT * FROM compra', conn).empty:
                # Inserción de datos del barrio
                df_barrio = df_file[['id_barrio', 'nombre_barrio']].drop_duplicates()
                for _, row in df_barrio.iterrows():
                    cursor.execute(constants.QUERY_INSERT_BARRIO, (row['id_barrio'], row['nombre_barrio']))

                # Inserción de datos de tipo de documento
                df_tipo_documento = df_file.copy().drop_duplicates('tipo_documento')
                for _, row in df_tipo_documento.iterrows():
                    cursor.execute(constants.QUERY_INSERT_TIPO_DOCUMENTO, (row['tipo_documento'], row['nombre_documento']))  
                
                # Inserción de datos de tipo de tienda
                df_tipo_tienda = df_file.copy().drop_duplicates('tipo_tienda')
                df_tipo_tienda['id_tienda'] = df_tipo_tienda['tipo_tienda'].apply(lambda x: constants.DICT_TIPO_TIENDA[x])
                for _, row in df_tipo_tienda.iterrows():
                    cursor.execute(constants.QUERY_INSERT_TIPO_TIENDA, (row['id_tienda'], row['tipo_tienda']))  
                
                # Inserción de datos de tienda
                df_tienda = df_file.copy().drop_duplicates('codigo_tienda')
                df_tienda['tipo_tienda'] = df_tienda['tipo_tienda'].apply(lambda x: constants.DICT_TIPO_TIENDA[x])
                for _, row in df_tienda.iterrows():
                    cursor.execute(constants.QUERY_INSERT_TIENDA, (row['codigo_tienda'], row['tipo_tienda'], row['id_barrio'], row['latitud_tienda'], row['longitud_tienda']))  

                # Inserción de datos de cliente
                df_cliente = df_file.copy().drop_duplicates('documento_cliente')
                for _, row in df_cliente.iterrows():
                    cursor.execute(constants.QUERY_INSERT_CLIENTE, (row['documento_cliente'], row['tipo_documento'], row['latitud_cliente'], row['longitud_cliente']))

                # Inserción de compra
                df_compra = df_file.copy()
                for _, row in df_compra.iterrows():
                    cursor.execute(constants.QUERY_INSERT_COMPRA, (row['documento_cliente'], row['codigo_tienda'], row['total_compra'], row['distancia_tienda_cliente'])) 

            conn.commit()
            conn.close()
    except Exception as e:
        print('Error: ',e)
        print(traceback.format_exc())
    return None