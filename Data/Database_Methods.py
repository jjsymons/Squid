import sqlite3
import os
import logging
from datetime import datetime

DATABASE_PATH = 'energy_usage.db'

def main():
    if not os.path.isfile(DATABASE_PATH):
        create_database()

def get_db_location():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, 'energy_usage.db')

def create_database():
    year = datetime.now().strftime('%Y')
    table_name = f"energy_usage_{year}"
    add_table(table_name)

def add_table(table_name):
    logging.basicConfig(filename='Logs\\data_insertions.log', level=logging.INFO)
    conn = None
    database_path = os.path.join(get_db_location())
    try:
        conn = sqlite3.connect(database_path)  
        cursor = conn.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (utc_datetime INTEGER, kWh_usage REAL, UNIQUE(utc_datetime))""")
        cursor.execute(f"""CREATE INDEX idx_energy_usage_timestamp ON {table_name} (utc_datetime)""")
    except sqlite3.Error as e:
        logging.error(f"{datetime.now()}: Database error: {e}")
    except sqlite3.Connection.Error as c:
        logging.error(f"{datetime.now()}: Connection error: {c}")
    finally:
        if conn:
            conn.close()

def insert_data(data_batch): 
    database_path = get_db_location()
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    logging.basicConfig(filename='Logs\\data_insertions.log', level=logging.INFO)

    #Temp hardcoding for table
    try:
        for data in data_batch:
            Date = data['Date']
            kWh = data['kWh']
            cursor.execute(f"""INSERT OR IGNORE INTO energy_usage_2024 (utc_datetime, kWh_usage) VALUES (?, ?)""", (Date, kWh))
            logging.info(f"{datetime.now()}: Inserted: utc_datetime={Date}, kWh_usage={kWh}")

    except sqlite3.Error as e:
            logging.error(f"{datetime.now()}: Insertion failed for {Date}: {e}")
    finally:
        conn.close()

if __name__ == '__main__':
    main()