import sqlite3
import pandas as pd
import Database_Methods as D_M
from datetime import datetime
from operator import itemgetter
import os 
import logging
from timeit import default_timer as timer

# File to take data requests to sqlite database and return them. #

def main():
    log_folder = os.path.abspath('../Logs')
    os.makedirs(log_folder, exist_ok=True)

    # Create log
    log_file = os.path.join(log_folder, 'data_processing.log')
    logging.basicConfig(filename=log_file, level=logging.INFO)
    data = read_database(20230331230000, 20230401003000)

    print(f"""Max: {find_max(data)}\nMin: {find_min(data)}\nAverage: {find_avg(data)}\nSum: {find_sum(data)}\n""")

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


# Testing section:
# Testing
def test():
    start = timer()
    max = find_max()
    end = timer()
    total_time = end - start
    print(f"Max: {total_time:.6f} seconds")

    start = timer()
    min = find_min(data)
    end = timer()
    total_time = end - start
    print(f"Min: {total_time:.6f} seconds")

    start = timer()
    avg = find_avg(data)
    end = timer()
    total_time = end - start
    print(f"Average: {total_time:.6f} seconds")

    start = timer()
    sum = find_sum(data)
    end = timer()
    total_time = end - start
    print(f"Sum: {total_time:.6f} seconds")

    # Outcomes from data 11/04/2024.
    # SUMMARY
    # Unless there is a more optimal solution that I have missed, the outcomes to the max find is very very slow. 
    # 6 times slower. 0.000742 Seconds
    #Max: (20231015120000, 2.558)
    #Min: (20230430043000, 0.063)
    #Average: 0.2651800102424021
    #Sum: 3106.8489999999833

    # Python code gives the following outputs on the full database:
    #Max: 0.000131 seconds
    #Min: 0.000130 seconds
    #Average: 0.000213 seconds
    #Sum: 0.000212 seconds

if __name__ == '__main__':
    main()
