# Bank Holidays
# This program prints all the Northern Ireland bank Holidays
# By Ignacio Riboldi

import requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()

# Each region events
nothernireland_events = data['northern-ireland']['events']
england_events = data['england-and-wales']['events']
scotland_events = data['scotland']['events']

# Event dates for other regions
england_dates = {event['date'] for event in england_events}
scotland_dates = {event['date'] for event in scotland_events}

# Filter events that are unique to Northern Ireland
unique_nothernireland_events = [
    event for event in nothernireland_events
    if event['date'] not in england_dates and event['date'] not in scotland_dates
]

# Print the unique events
for event in unique_nothernireland_events:
    print(f"{event['date']} - {event['title']}")
