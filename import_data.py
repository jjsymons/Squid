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
        database_utc_time = int(dt_utc.strftime("%Y%m%d%H%M%S"))
        
        processed_data.append({'Date': database_utc_time, 'kWh': float("{:.3f}".format(float(kWh)))})
        i+=1
    return processed_data


data = import_data('.\\Data\\data.csv')
print(clean_data(data))



