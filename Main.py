import Scripts.Import_Data as I_D
import Data.Database_Methods as D_M

def main():
    D_M.main()
    processed_data = I_D.main()
    D_M.insert_data(processed_data)



if __name__ == '__main__':
    main()