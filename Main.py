import Scripts.Import_Data as I_D
import Data.Database_Methods as D_M
import Data.Data_Processing as D_P
from datetime import datetime

def main():
    #D_M.main()
    #print(D_M.get_db_location())
    #processed_data = I_D.main()
    #D_M.insert_data(processed_data)
    D_P.main()



if __name__ == '__main__':
    main()