import json
import pandas as pd


with open("tea_inventory.json", "r") as f:
    tea_inv = json.load(f)


with open("cln_ord_data.json", "r") as f:
    orders = json.load(f)


skus = []

for i in tea_inv:
    #i["ord_amount"] = amount
    for b in i["skus"]:
        sku = b
        skus.append(sku)
tea_orders = []
for z in orders:
    if z["product_sku"] in skus:
        tea_orders.append(z)


with open("tea_orders.json", "w") as f:
    json.dump(tea_orders, f)
print(tea_orders)