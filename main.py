# Description: Main file to create the data warehouse and execute the ETL process.

import os
import pandas as pd
from Components import db
from Components import load

# Define paths

data_path = 'golden_stage'
db_path = 'DB'

# Variables

db_name = 'sales.db'

# Execution
if __name__ == '__main__':
    # Read data from an Excel file into a Pandas DataFrame
    df = pd.read_excel(os.path.join(data_path, 'sales_dataset_golden.xlsx'))

    # Create the data warehouse by calling the create_db function from the db module
    db.create_db(db_name, db_path)

    # Insert the data into the data warehouse by calling the insert_data function from the load module
    load.insert_data(df, db_name, db_path)
