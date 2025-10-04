# Bank Holidays
# This program prints all the Northern Ireland bank Holidays
# By Ignacio Riboldi

import requests

url = "https://www.gov.uk/bank-holidays.json"
response = requests.get(url)
data = response.json()

# Events by region
northern_ireland_events = data['northern-ireland']['events']
england_events = data['england-and-wales']['events']
scotland_events = data['scotland']['events']

# Titles in other regions
england_titles = {event['title'] for event in england_events}
scotland_titles = {event['title'] for event in scotland_events}

# Filter unique titles
unique_titles = set()

for event in northern_ireland_events:
    title = event['title']
    if title not in england_titles and title not in scotland_titles:
        unique_titles.add(title)

for title in unique_titles:
    print(title)
