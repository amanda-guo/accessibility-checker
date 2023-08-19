from taipy.gui import Gui, notify, navigate
from dotenv import load_dotenv
import requests
import os
import requests
import json

#  WAVE api key
load_dotenv()
api_key = os.getenv("API_KEY")
url = os.getenv("URL")
report_type = 1

# get data from WAVE api in json format

# store general errors
errors_array = []

# store contrast errors
contrast_errors_array = []

# store other alerts
alerts_array = []

# get data from WAVE api in json format

text = "https://www.google.com"
page1_md = """
# Accesibility Checker 
# Enter the URL of your website to easily perform an accessibility check

My text: <|{text}|>

<|{text}|input|>

<|Check|button|on_action=on_button_action|>
"""

response = None

page2_md = "## Accessibility Visualization"

pages = {
    "page1": page1_md,
    "page2": page2_md
}

def pretty_print():
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


def on_button_action(state):
    global response
    notify(state, 'info', f'The text is: {state.text}')
    pretty_print()
    navigate(state, "page2")

def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.text = ""
        return

Gui(pages=pages).run(use_reloader=True, port=5001)
