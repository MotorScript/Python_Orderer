import json
from operator import contains
import re


with open("inventory_data.json", "r") as f:
    inventory = json.load(f)


# def find(b):
#     for i in inventory:
#         is_oz = i["name"].contains("tea")
#     return is_oz
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
    "SQ0337763",
    "SQ3762489",
    "SQ1822596",
    "SQ6223323"

]
tea_bag_sku = [
    "SQ5828001",
    "SQ6424180"
]

inv_data =[]

for i in inventory:
    contains_keyword = str(i["name"]).lower().__contains__("candle") or str(i["name"]).lower().__contains__("honey")
    
    if str(i["variantAttributes"]).strip(r"[']").lower()=="size" or str(i["variantAttributes"]).strip(r"[']").lower()=="sizes":
        if i["variants"][0]["sku"] not in sku_ignore and contains_keyword != True and i["variants"][0]["sku"].__contains__("SQ"):
            sku = []
            sizes = []
            for b in i["variants"]:

                sku.append(b["sku"])
                sizes.append(b["attributes"]["Size"])
            
            if b["sku"] not in tea_bag_sku:
                try:
                    for a in sizes:
                        index = sizes.index(a)
                        num = re.findall(r'\d+', sizes[index])
                        num = list(map(int, num))
                        s = [str(i) for i in num]
                        res = "".join(s)
                        num = int(res)
                        
                        sizes[index] = num
                except TypeError:
                    continue
            
            name = i["name"]
            #index = i["variants"].index("attributes")
            #print(sku, sizes)
           

            inv_data_json = {
                "name": name,
                "skus": sku,
                "sizes": sizes
            }
            inv_data.append(inv_data_json)
            #print(name)
    #if i["name"] == "100% RAW MULTI PURPOSE AFRICAN BLACK SOAP!":
        #print(i["variants"][0]["sku"])

with open("tea_inventory.json", "w") as f:
    json.dump(inv_data, f)