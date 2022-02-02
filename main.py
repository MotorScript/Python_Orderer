from sys import api_version
import requests
from dotenv import load_dotenv
import os
import json
import re


load_dotenv()
api_key = os.getenv("API_KEY")
sku_ignore = [
    "SQ1075621",
    "SQ3778713",
    "SQ7841246",
    "SQ2446135",
    "SQ6791812",
    "SQ5744355",
    "SQ6436091",
    "SQ5185507",
    "SQ0337127",
    "SQ0930812",
    "SQ0992375",
    "SQ2249708",
    "SQ3148606",
    "SQ6185413",
    "SQ7278641",
    "SQ8855090",
    "SQ1566067",
    "SQ6156653",
    "SQ9195365",
    "SQ0719627",
    "SQ6757299",
    "SQ9168111",
    "SQ7602344",
    "SQ6797461",
    "SQ9185055",
    "SQ9615602",
    "SQ7997711",
    "SQ0894977",
    "SQ9942636",
    "SQ9212935",
    "SQ4132594",
    "SQ0768242",
    "SQ9927198",
    "SQ1580378",
    "SQ8250644",
    "SQ6450618",
    "SQ9218838",
    "SQ7291909",
    "SQ1590376",
    "SQ4640135",
    "SQ4519920",
    "SQ1329107",
    "SQ3607988",
    "SQ2190479",
    "SQ4699753",
    "SQ0337763"

]
tea_sku = [
    "SQ9559552",
    "SQ9396906",
    "SQ6832447",
    "SQ9452382",
    "SQ6599715",
    "SQ8779714",
    "SQ6010692",
    "SQ9023182",
    "SQ8153046",
    "SQ5554145",
    "SQ7325242",
    "SQ4091978",
    "SQ2225339",
    "SQ4010512",
    "SQ1646863",
    "SQ4083116",
    "SQ1914789",
    "SQ2535315",
    "SQ8039925",
    "SQ1521954",
    "SQ9739867",
    "SQ7855626",
    "SQ3326399",
    "SQ0526499",
    "SQ8546204",
    "SQ9151704",
    "SQ1216335",
    "SQ9525719",
    "SQ8978865",
    "SQ5782420",
    "SQ0733874",
    "SQ4661584",
    "SQ0670252",
    "SQ9811864",
    "SQ2766507",
    "SQ9181994",
    "SQ6949240",
    "SQ3979895",
    "SQ5357669",
    "SQ1253643"

]

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
jsonList = []
jsonList.append(requests.get(f"https://api.squarespace.com/{apiversion}/{resourcepath+resourcepath3}", headers=data).json())
jsonList.append(requests.get(f"https://api.squarespace.com/{apiversion}/{resourcepath+resourcepath3}?&cursor={cursor}", headers=data).json())

#req = requests.get(f"https://api.squarespace.com/{apiversion}/{resourcepath+resourcepath2}?&fulfillmentStatus={status}", headers=data)

with open("inventory_data.json", "w") as f:
    json.dump(jsonList, f)

with open("orders_data.json", "r") as f:
    orders = json.load(f)
with open("inventory_data.json", "r") as f:
    inventory = json.load(f)
order_product_data = {}
order_data = []
order_skus = []
len = int(len(orders["result"]))
for i in orders["result"][:len]:
    
    for b in i["lineItems"]:
        
        if b["sku"] in sku_ignore:
            continue
        elif b["sku"] in order_skus:
            for i in order_data:
                i["product_quantity"] += b["quantity"]
            print("in elif")
        else:
            order_product_data = {
                "product_name": b["productName"],
                "product_quantity": b["quantity"],
                "product_sku": b["sku"]
            }
            for a in b["variantOptions"]:
                num = 0 
                try:
                    num = re.findall(r'\d+', a["value"])
                    num = list(map(int, num))
                    s = [str(i) for i in num]
                    res = "".join(s)
                    num = int(res)
                except:
                    num = "NA"
                order_product_data["product_size"] = num
            order_data.append(order_product_data)

total_ammount = 0
for i in order_data:
    order_skus.append(i["product_sku"])
    
    try:
        if i["product_size"] != "NA":
            total_ammount = i["product_size"] * i["product_quantity"]
            i["total_ammount"] = total_ammount
            #print(total_ammount)
        else:
            continue
            #print("Product does not have a valid size.")
    except KeyError:
        continue
       # print("No product size available")
#print(order_data)

#print(order_data[:]["product_sku"])
#print(order_skus)


for i in inventory:
    for b in i["products"]:

        print(b["name"])