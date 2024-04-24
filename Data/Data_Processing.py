import sqlite3
from Database_Methods import get_db_location
from datetime import datetime
from operator import itemgetter
import os 
import logging
from timeit import default_timer as timer

# File to take data requests to sqlite database and return them.

# Do an additional test in future to check the time taken to read the database and then compute in Python
# Then compare to just checking for the values in SQL

def main():
    log_folder = os.path.abspath('../Logs')
    os.makedirs(log_folder, exist_ok=True)

    # Create log
    log_file = os.path.join(log_folder, 'data_processing.log')
    logging.basicConfig(filename=log_file, level=logging.INFO)
    return read_database(20230331230000, 20230401003000)
    #print(f"""Max: {find_max(data)}\nMin: {find_min(data)}\nAverage: {find_avg(data)}\nSum: {find_sum(data)}\n""")

# Function for opening the database

def read_database(start_date, end_date):
    conn = None
    database_path = get_db_location()
    try:
        conn = sqlite3.connect(database_path)  
        cursor = conn.cursor()
        # Need to create system for unification depending on start / end dates. 
        # Hard Coded for time being
        cursor.execute(f"""SELECT utc_datetime, kWh_usage FROM energy_usage_2024 WHERE utc_datetime BETWEEN ? AND ?;""", (start_date, end_date))
        logging.debug(f"Executing query with parameters: {start_date}, {end_date}")
        rows = cursor.fetchall()
        return rows
    except sqlite3.Error as e:
        logging.error(f"{datetime.now()}: Sqlite error: {e}")
        return None
    finally:
        if conn:
            conn.close()

def find_max(data):
    return max(data, key = itemgetter(1))

def find_min(data):
    return min(data, key=itemgetter(1)) 

def find_avg(data):
    total = 0
    for items in data:
        total += items[1]
    return total/len(data)
    
def find_sum(data):
    total = 0
    for items in data:
        total += items[1]
    return total


if __name__ == '__main__':
    main()
