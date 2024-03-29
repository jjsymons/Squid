from datetime import datetime, timezone
def import_data(fileName):
    with open(fileName, 'r') as file:
        data = file.readlines()
    return data

def clean_data(data):
    processed_data = []

    i = 1
    while i < len(data):
        # Split line into 3 sections, so that the datetime can be examined. 
        # Do the same with the prior line
        kWh, date, _ = data[i].split(',')
        
        
        dt_bst = datetime.fromisoformat(date)
        dt_utc = dt_bst.astimezone(timezone.utc)
        kWh = float(kWh)
        
        processed_data.append({'Date': dt_utc, 'kWh': "{:.3f}".format(kWh)})
        i+=1
    return processed_data


data = import_data('.\\Data\\data.csv')
print(clean_data(data))



