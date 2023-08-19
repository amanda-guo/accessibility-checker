from taipy.gui import Gui
from dotenv import load_dotenv
import requests
import os
import pandas as pd

#  WAVE api key
load_dotenv()
api_key = os.getenv("API_KEY")
url = os.getenv("URL")

# get data from WAVE api in json format
response = requests.get(f'https://wave.webaim.org/api/request?key={api_key}&reporttype=3&url={url}')
if response.ok:
    data = response.json()
    print(data)

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

Gui(page).run(use_reloader=True, port=5001)