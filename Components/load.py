from constants import constants
import pandas as pd
import os
import sqlite3
import traceback

def insert_data(df_file, db_name, db_path):
    """
    Inserts data from a DataFrame into a SQLite database.

    Parameters:
    - df_file (pandas.DataFrame): The DataFrame containing the data to be inserted.
    - db_name (str): The name of the SQLite database.
    - db_path (str): The path to the directory where the SQLite database is located.

    Returns:
    None
    """
    try:
        # Check if the SQLite database file exists
        if os.path.exists(os.path.join(db_path, db_name)):
            # Connect to the SQLite database
            conn = sqlite3.connect(os.path.join(db_path, db_name))
            cursor = conn.cursor()
            
            # Check if the 'compra' table in the database is empty
            if pd.read_sql('SELECT * FROM compra', conn).empty:
                # Insert data into the 'barrio' table
                df_barrio = df_file[['id_barrio', 'nombre_barrio']].drop_duplicates()
                for _, row in df_barrio.iterrows():
                    cursor.execute(constants.QUERY_INSERT_BARRIO, (row['id_barrio'], row['nombre_barrio']))

                # Insert data into the 'tipo_documento' table
                df_tipo_documento = df_file.copy().drop_duplicates('tipo_documento')
                for _, row in df_tipo_documento.iterrows():
                    cursor.execute(constants.QUERY_INSERT_TIPO_DOCUMENTO, (row['tipo_documento'], row['nombre_documento']))  
                
                # Insert data into the 'tipo_tienda' table
                df_tipo_tienda = df_file.copy().drop_duplicates('tipo_tienda')
                df_tipo_tienda['id_tienda'] = df_tipo_tienda['tipo_tienda'].apply(lambda x: constants.DICT_TIPO_TIENDA[x])
                for _, row in df_tipo_tienda.iterrows():
                    cursor.execute(constants.QUERY_INSERT_TIPO_TIENDA, (row['id_tienda'], row['tipo_tienda']))  
                
                # Insert data into the 'tienda' table
                df_tienda = df_file.copy().drop_duplicates('codigo_tienda')
                df_tienda['tipo_tienda'] = df_tienda['tipo_tienda'].apply(lambda x: constants.DICT_TIPO_TIENDA[x])
                for _, row in df_tienda.iterrows():
                    cursor.execute(constants.QUERY_INSERT_TIENDA, (row['codigo_tienda'], row['tipo_tienda'], row['id_barrio'], row['latitud_tienda'], row['longitud_tienda']))  

                # Insert data into the 'cliente' table
                df_cliente = df_file.copy().drop_duplicates('documento_cliente')
                for _, row in df_cliente.iterrows():
                    cursor.execute(constants.QUERY_INSERT_CLIENTE, (row['documento_cliente'], row['tipo_documento'], row['latitud_cliente'], row['longitud_cliente']))

                # Insert data into the 'compra' table
                df_compra = df_file.copy()
                for _, row in df_compra.iterrows():
                    cursor.execute(constants.QUERY_INSERT_COMPRA, (row['documento_cliente'], row['codigo_tienda'], row['total_compra'], row['distancia_tienda_cliente'])) 

            # Commit changes and close the connection
            conn.commit()
            conn.close()
    except Exception as e:
        # Print error details and traceback if an exception occurs
        print('Error: ', e)
        print(traceback.format_exc())
    return None
