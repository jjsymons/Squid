import sqlite3
import pandas as pd
import Database_Methods as D_M
from datetime import datetime
import logging

# File to take data requests to sqlite database and return them. #

def main():
    # Create log
    logging.basicConfig(filename='Logs\\data_processing.log', level=logging.INFO)
    print(read_database(20230331230000, 20230401003000))
    # Create Database if not found

# Function for opening the database

def read_database(start_date, end_date):
    conn = None
    database_path = D_M.get_db_location()
    try:
        conn = sqlite3.connect(database_path)  
        cursor = conn.cursor()
        # Need to create system for unification depending on start / end dates
        cursor.execute(f"""SELECT utc_datetime, kWh_usage FROM energy_usage_2024 WHERE kWh_usage BETWEEN {start_date} AND {end_date};""")
    except sqlite3.Connection.Error as c:
        logging.error(f"{datetime.now()}: Connection error: {c}")
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    main()



# funtion for reading the database with a specified time period






    

