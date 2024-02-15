#!/usr/bin/python3


import requests
import json

# Your Datadog API and Application keys
api_key = 'b716ad23714fffd469899721057dfeae'
app_key = '7e79c2b9ae4be84cdaeb7266b1ed383184e9ff0a'

# Headers for API requests
headers = {
    'Content-Type': 'application/json',
    'DD-API-KEY': api_key,
    'DD-APPLICATION-KEY': app_key
}

# Create a new dashboard
dashboard_data = {
    "title": "My New Dashboard",
    "layout_type": "ordered",
    "widgets": [
        {
            "definition": {
                "type": "timeseries",
                "requests": [
                    {"q": "avg:system.cpu.idle{*}"}
                ],
                "title": "CPU Idle"
            }
        },
        {
            "definition": {
                "type": "timeseries",
                "requests": [
                    {"q": "avg:system.load.1{*}"}
                ],
                "title": "Load Average"
            }
        },
        {
            "definition": {
                "type": "query_value",
                "requests": [
                    {"q": "avg:system.disk.used{*}"}
                ],
                "title": "Disk Used"
            }
        },
        {
            "definition": {
                "type": "query_value",
                "requests": [
                    {"q": "avg:system.memory.used{*}"}
                ],
                "title": "Memory Used"
            }
        }
    ]
}

# Create the dashboard
response = requests.post('https://api.datadoghq.com/api/v1/dashboard', headers=headers, data=json.dumps(dashboard_data))

# Check if the dashboard was successfully created
if response.status_code == 200:
    dashboard_id = response.json()['id']
    print("Dashboard created successfully with ID:", dashboard_id)

    # Writing the dashboard ID to the answer file
    with open('2-setup_datadog', 'w') as f:
        f.write(str(dashboard_id))
else:
    print("Failed to create dashboard. Status code:", response.status_code)
    print("Response:", response.text)

