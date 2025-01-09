import requests
import json

# API URL and Headers
url = "https://api.sportradar.com/rugby-union/trial/v3/en/sport_events/sr%3Asport_event%3A51961135/timeline.json?api_key=zmn9XB45EPJip6QJdMPluv3mEx7XMj0UapeXsGUj"
headers = {"accept": "application/json"}

# Fetch the data
response = requests.get(url, headers=headers)

# Check response status
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    
    # Save the data to a JSON file
    with open("ulster_connacht_timeline.json", "w") as json_file:
        json.dump(data, json_file, indent=4)
    
    print("Data successfully saved to 'ulster_connacht_timeline.json'!")
else:
    print(f"Error fetching data: {response.status_code}")
