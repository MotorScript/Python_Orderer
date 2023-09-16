import requests
from dotenv import load_dotenv
import os
import json
import modules
import sqlite3

load_dotenv()
api_key = os.getenv("API_KEY")

apiversion = "1.0"
resourcepath = "commerce/"
resourcepath2 = "orders"
resourcepath3 = "products"
description = "PythonProject"
status = "PENDING"
cursor = "eyJzZXJ2aWNlQ3Vyc29yIjoiTlRBIiwibW9kaWZpZWRBZnRlciI6bnVsbCwibW9kaWZpZWRCZWZvcmUiOm51bGwsInF1ZXJ5IjpudWxsfQ"
data = {
    "Authorization": f"Bearer {api_key}",
    "User-Agent": f"{description}"
}
pull_info = False

if pull_info:
    ws = requests.get("https://docs.google.com/document/d/1FFy3NMaQAYP051l9PW7Ay3LIjRepO_3Q/edit?usp=sharing&ouid=103141353685442283849&rtpof=true&sd=true")
    res = requests.get(f"https://api.squarespace.com/{apiversion}/{resourcepath+resourcepath3}", headers=data).json() 
    res2 = requests.get(f"https://api.squarespace.com/{apiversion}/{resourcepath+resourcepath3}?&cursor={cursor}", headers=data).json()
    res3 = {**res, **res2}
    
    # inv_list = res["products"] + res2["products"]
    req = requests.get(f"https://api.squarespace.com/{apiversion}/{resourcepath+resourcepath2}?&fulfillmentStatus={status}", headers=data).json()
    with open("inventory_data.json", "w") as f:
        json.dump(res3, f, indent=2)

    with open("orders_data.json", "w") as f:
        json.dump(req, f, indent=2)


tea_inv = modules.get_tea()

modules.order_items(tea_inv, True)

# modules.create_worksheet("tea_inventory.json")

