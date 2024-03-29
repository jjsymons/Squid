import sqlite3
import os

DATABASE_PATH = 'squidDatabase.db'

def main():
    if not os.path.isfile(DATABASE_PATH):
        create_database()

#def create_database():
    #conn = sqlite3.connect(DATABASE_PATH)
    #cursor = conn.cursor()
    # Next step is to build the general database file.
    # Format should be table for each year, to reduce processing times, Perhaps a link between each month.
    # Table should look like: YEAR and inside it Date:Datetime, Month, Week No, kWH

if __name__ == '__main__':
    main()