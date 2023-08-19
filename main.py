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

# declaring data variables
data_errors = {}
data_values = {}

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

# Putting the data into simple bar and pie charts

def visualizing_errors():
    
    # Errors

    typeOfError = []
    numberOfErrors = []

    for error in errors_array:
        typeOfError.append(error["id"])
        numberOfErrors.append(error["count"])

    for error in contrast_errors_array:
        typeOfError.append(error["id"])
        numberOfErrors.append(error["count"])

    dataErrors = {
        "Type of Error": typeOfError,
        "Number of Errors": numberOfErrors
    }

    # Alerts

    typeOfAlert = []
    numberOfAlerts = []

    for alert in alerts_array:
        typeOfAlert.append(alert["id"])
        numberOfAlerts.append(alert["count"])

    dataAlerts = {
        "Type of Alert": typeOfAlert,
        "Number of Alerts": numberOfAlerts
    }

    print("EXECUTED THIS FUNCTION")

    return dataErrors, dataAlerts

def on_button_action(state):
    global response
    notify(state, 'info', f'The text is: {state.text}')
    pretty_print()
    navigate(state, "page2")
    result = visualizing_errors()
    data_errors = result[0]
    data_alerts = result[1]

def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.text = ""
        return


page2_md = """

## Accessibility Visualization

# Bar graph for errors

<|{data_errors}|chart|type=bar|x=Type of Error|y=Number of Errors|>

# Pie chart for errors

<|{data_errors}|chart|type=pie|values=Number of Errors|label=Type of Error|>

# Bar graph for alerts

<|{data_alerts}|chart|type=bar|x=Type of Alert|y=Number of Alerts|>

# Pie chart for alerts

<|{data_alerts}|chart|type=pie|values=Number of Alerts|label=Type of Alert|>

"""

pages = {
    "page1": page1_md,
    "page2": page2_md
}

Gui(pages=pages).run(use_reloader=True, port=5001)
