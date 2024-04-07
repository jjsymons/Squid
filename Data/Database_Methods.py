import sqlite3
import os
import logging
from datetime import datetime

def main():
    # Create log
    logging.basicConfig(filename='Logs\\data_insertions.log', level=logging.INFO)
    # Create Database if not found
    if not os.path.isfile(get_db_location()):
        create_database()

def get_db_location():
    # For future installation, find where the database is installed
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, 'energy_usage.db')

def create_database():
    # Creates initial database to use with an initial table for the given year
    year = datetime.now().strftime('%Y')
    table_name = f"energy_usage_{year}"
    # Calls to create a table
    add_table(table_name)

def add_table(table_name):
    conn = None
    database_path = get_db_location()
    try:
        conn = sqlite3.connect(database_path)  
        cursor = conn.cursor()
        # Creates a table if the called table doesn't exist. utc_datetime is unique to avoid duplicates
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS energy_usage_2024 (utc_datetime INTEGER, kWh_usage REAL, UNIQUE(utc_datetime))""")
        # Checks if the table has an index if not creates one
        cursor.execute(f"""SELECT name FROM sqlite_master WHERE type='index' AND name='idx_energy_usage_{table_name}_timestamp'""")
        if not cursor.fetchone():
            cursor.execute(f"""CREATE INDEX idx_energy_usage_{table_name}_timestamp ON {table_name} (utc_datetime)""")
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

    try:
        for data in data_batch:
            # Reads from data_batch which is a list of dictionaries [{'Date': 20230331230000,'kWh': 0.125}, {'Date': 20230331233000,'kWh': 0.625}...]
            Date = data['Date']
            kWh = data['kWh']          
            # Checks for duplicates, inserts if none found
            cursor.execute("SELECT EXISTS(SELECT 1 FROM energy_usage_2024 WHERE utc_datetime=?)", (Date,))
            if cursor.fetchone()[0]:
                print(f"Duplicate timestamp: {Date} already exists. Skipping insertion.")
            else:
                cursor.execute(f"""INSERT OR IGNORE INTO energy_usage_2024 (utc_datetime, kWh_usage) VALUES (?, ?)""", (Date, kWh))
                logging.info(f"{datetime.now()}: Inserted: utc_datetime={Date}, kWh_usage={kWh}")
                conn.commit()
    except sqlite3.Error as e:
            logging.error(f"{datetime.now()}: Insertion failed for {Date}: {e}")
            print("Insertion Error:", e)
    finally:
        conn.close()

if __name__ == '__main__':
    main()