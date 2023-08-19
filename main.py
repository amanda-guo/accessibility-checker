from taipy.gui import Gui
from dotenv import load_dotenv
import requests
import os
import pandas as pd

#  WAVE api key
load_dotenv()
api_key = os.getenv("API_KEY")
url = os.getenv("URL")

# store general errors
errors_array = []

# store contrast errors
contrast_errors_array = []

# store other alerts
alerts_array = []

# get data from WAVE api in json format
response = requests.get(f'https://wave.webaim.org/api/request?key={api_key}&reporttype=2&url={url}')
if response.ok:
    data = response.json()
    
    # credits remaining
    print("Credits Remaining:")
    print(data['statistics']['creditsremaining'])

    # STORE GENERAL ERRORS
    errors = data["categories"]["error"]["items"]
    for type, item in errors.items():
        error_item = {
            "id": item["id"],
            "description": item["description"],
            "count": item["count"]
        }
        errors_array.append(error_item)
    
    # print general errors
    print("GENERAL ERRORS:")
    for error in errors_array:
        print("Type of Error: " + error["id"])
        print("Error Description: " + error["description"])
        print("Number of Errors: " + str(error["count"]))
        print()

    # STORE CONTRAST ERRORS
    contrast_errors = data["categories"]["contrast"]["items"]
    for type, item in contrast_errors.items():
        error_item = {
            "id": item["id"],
            "description": item["description"],
            "count": item["count"]
        }
        contrast_errors_array.append(error_item)
    
    # print contrast errors
    print("CONTRAST ERRORS")
    for error in contrast_errors_array:
        print("Type of Error: " + error["id"])
        print("Error Description: " + error["description"])
        print("Number of Errors: " + str(error["count"]))
        print()

    # store alerts
    alerts = data["categories"]["alert"]["items"]
    for type, item in alerts.items():
        error_item = {
            "id": item["id"],
            "description": item["description"],
            "count": item["count"]
        }
        alerts_array.append(error_item)
    
    # print alerts
    print("ALERTS")
    for error in alerts_array:
        print("Type of Error: " + error["id"])
        print("Error Description: " + error["description"])
        print("Number of Errors: " + str(error["count"]))
        print()

    

value = 10

page = """
#Our Very First Taipy Application
#Testing out branch commit

<|layout|columns=1 1 1|

<|first column
<|container container-styling|
###Slider 1 <br/>
Slider value: <|{value}|> <br/>
<|{value}|slider|>
|>
|>

<|second column
<|container container-styling|
###Slider 2 <br/>
Slider value: <|{value}|> <br/>
<|{value}|slider|>
|>
|>

<|third column
<|container container-styling|
###Slider 3 <br/>
Slider value: <|{value}|> <br/>
<|{value}|slider|>
|>
|>
|>

"""

from taipy.gui import Gui
import requests
import json

Gui(page = "BIG ASS DATA").run(dark_mode=True) # use_reloader=True

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


response = requests.get("https://wave.webaim.org/api/request?key=kw1MFx7w3380&reporttype=2&url=https://google.com/")
jprint(response.json())

Gui(page).run(use_reloader=True, port=5001)