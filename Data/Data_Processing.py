import sqlite3
import pandas as pd
import Database_Methods as D_M
from datetime import datetime
import os 
import logging

# File to take data requests to sqlite database and return them. #

def main():
    log_folder = os.path.abspath('../Logs')
    os.makedirs(log_folder, exist_ok=True)
    
    log_folder = os.path.abspath('../Logs')
    os.makedirs(log_folder, exist_ok=True)
    # Create log
    log_file = os.path.join(log_folder, 'data_processing.log')
    logging.basicConfig(filename=log_file, level=logging.info)
    print(read_database(20230331230000, 20230401003000))
    # Create Database if not found

# Function for opening the database

def read_database(start_date, end_date):
    conn = None
    database_path = D_M.get_db_location()
    try:
        conn = sqlite3.connect(database_path)  
        cursor = conn.cursor()
        # Need to create system for unification depending on start / end dates. 
        # Hard Coded for time being
        cursor.execute(f"""SELECT utc_datetime, kWh_usage FROM energy_usage_2024 WHERE utc_datetime BETWEEN ? AND ?;""", (start_date, end_date))
        logging.debug(f"Executing query with parameters: {start_date}, {end_date}")
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as c:
        logging.error(f"{datetime.now()}: Connection error: {c}")
        return None
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    main()



# funtion for reading the database with a specified time period






    

