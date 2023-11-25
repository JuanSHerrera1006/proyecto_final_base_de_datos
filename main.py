# Description: Main file to create the data warehouse and execute the ETL process.

import os
import pandas as pd
from Components import db
from Components import load

# Define paths

data_path = 'golden_stage'
db_path='DB'

# Variables

db_name = 'sales.db'

# Execution
if __name__ == '__main__':
    df = pd.read_excel(os.path.join(data_path, 'sales_dataset_golden.xlsx'))
    # Create the data warehouse
    db.create_db(db_name,db_path)
    # Insert the data into the data warehouse
    load.insert_data(df,db_name, db_path)
