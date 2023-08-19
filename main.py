from taipy.gui import Gui, notify, navigate
from dotenv import load_dotenv
import requests
import os
import requests
import json


text = "https://www.google.com"

page1_md = """
# Accesibility Checker INC. 
# Enter the URL of your website to perform an accessibility check

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


def on_button_action(state):
    global response
    notify(state, 'info', f'The text is: {state.text}')
    response = requests.get(f'https://wave.webaim.org/api/request?key={api_key}&reporttype={report_type}&url={text}')
    if response is not None:
        print("Response Status Code:", response.status_code)
        navigate(state, "page2")





def on_change(state, var_name, var_value):
    if var_name == "text" and var_value == "Reset":
        state.text = ""
        return

#  WAVE api key
load_dotenv()
api_key = os.getenv("API_KEY")
url = os.getenv("URL")
report_type = 1

# get data from WAVE api in json format


Gui(pages=pages).run(use_reloader=True, port=5001)
