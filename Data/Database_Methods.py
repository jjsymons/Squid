import sqlite3
import os
from datetime import datetime

DATABASE_PATH = 'squid_Database.db'

def main():
    if not os.path.isfile(DATABASE_PATH):
        create_database()

def create_database():
    year = datetime.now().strftime('%Y')
    table_name = f"energy_usage_{year}"
    add_table(table_name)

def add_table(table_name):
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        cursor = conn.cursor()
        cursor.execute(f"""CREATE TABLE IF NOT EXISTS {table_name} (utc_datetime INTEGER, kWh_usage REAL, UNIQUE(utc_datetime))""")
        cursor.execute(f"""CREATE INDEX idx_energy_usage_timestamp ON {table_name} (utc_datetime)""")
    except sqlite3.Error as e:
        print("Database error:", e)
    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    main()