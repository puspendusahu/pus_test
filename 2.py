# 2. API IntegraƟon and JSON Handling (15 minutes)
# Task:
# Write a Python script to interact with a weather API (mock the response if needed).
# Requirements:
# 1. Fetch weather data for mulƟple ciƟes (e.g., "Hyderabad", "Mumbai", "Delhi").
# 2. Save the data in a JSON file with the following format:
# json
# Copy code
# {
#  "city": "Hyderabad",
#  "temperature": 30,
#  "humidity": 60
# }
# 3. Ensure the script retries the API request if it fails due to a Ɵmeou


import requests
import json

cities = ["Hyderabad", "Mumbai", "Delhi"]

for city in cities:
    url = f"{city}" # currect api url we have to used with city
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        with open(f"{city}.json", "w") as f:
            json.dump(data, f)
    else:
        print(f"Failed to fetch data for {city}. Status code: {response.status_code}")