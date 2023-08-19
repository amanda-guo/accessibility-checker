from taipy.gui import Gui
import pandas as pd

value = 10

page = """
#Our Very First Taipy Application

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