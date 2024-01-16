from datetime import datetime
import requests
import os

api_key = os.environ['REDASH_API_KEY']
url = f"https://redash.masterworks.com/api/admin/queries/outdated?api_key={api_key}"
api_response = requests.get(url).json()
if 'updated_at' in api_response:
    updated_at_epoch = float(api_response['updated_at'])
    #Convert Epoch time to datetime
    updated_at_datetime = datetime.utcfromtimestamp(updated_at_epoch)

    #Get Current time in datetime
    current_time = datetime.utcnow()
    time_difference = current_time - updated_at_datetime

    if time_difference.total_seconds() > 10 * 60:
        exit(1)
        print("The 'updated_at' value is older than 30 mintues.")
    else:
        print("The 'updated_at' value is within the last 30 minutes")
else:
    print('Error: There is no updated_at')

