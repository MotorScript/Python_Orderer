from sys import api_version
import requests
from dotenv import load_dotenv
import os
import json
import re
load_dotenv()
api_url = os.getenv("API_KEY")
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

apiversion = "1.0"
resourcepath = "commerce/orders"
description = "PythonProject"
status = "PENDING"
data = {
    "Authorization": f"Bearer {api_url}",
    "User-Agent": f"{description}"
}

#req = requests.get(f"https://api.squarespace.com/{apiversion}/{resourcepath}?&fulfillmentStatus={status}", headers=data)

#with open("orders_data.json", "w") as f:
#    json.dump(req.json(), f)

with open("orders_data.json", "r") as f:
    orders = json.load(f)

order_product_data = {}
order_data = []
len = int(len(orders["result"]))
for i in orders["result"][:len]:
    for b in i["lineItems"]:
        if b["sku"] in sku_ignore:
            continue
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

print(order_data)
total_ammount = 0
for i in order_data:
    
    try:
        if i["product_size"] != "NA":
            total_ammount = i["product_size"] * i["product_quantity"]
            print(total_ammount)
        else:
            print("Product does not have a valid size.")
    except KeyError:
        print("No product size available")
