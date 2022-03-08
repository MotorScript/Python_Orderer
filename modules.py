
import json
import re
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os
import pandas as pd

def total(inv, orders):
    for order in orders:
        name = order['product_name']
        amount = int(order["product_size"] * order["product_quantity"])
        for item in inv:
            if "ordered_amount" not in item.keys():
                    item["ordered_amount"] = 0

            if item['name'] == name:
                if item["ordered_amount"] == 0:
                    item["ordered_amount"] = amount
                else:
                    item["ordered_amount"] += amount     
            
                
            
                
    return inv


def get_tea():
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
        "SQ9321265",
        "SQ9376209",
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
    
    with open("order_ignore.json", "r") as f:
        order_ignore = json.load(f)
    with open("orders_data.json", "r") as f:
        orders = json.load(f)
    with open("inventory_data.json", "r") as f:
        inventory = json.load(f)
    with open("tea_inventory.json", "r") as f:
        tea_inv = json.load(f)
   
    order_product_data = {}
    order_data = []
    tea_orders = []

    length = int(len(orders["result"]))
    for i in orders["result"][:length]:
        order_number = i["orderNumber"]
        if order_number in order_ignore:
            break
        else:
            for b in i["lineItems"]:
                if b["sku"] in sku_ignore:
                    break
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
                        order_product_data["size_des"] = a["value"]
                    order_data.append(order_product_data)
        order_ignore.append(order_number)
    for order in order_data:
        if order["product_sku"] in tea_sku:
            tea_orders.append(order)
    new_inv = total(tea_inv, tea_orders)
    with open("order_ignore.json", "w") as f:
        json.dump(order_ignore, f, indent=2)
    with open("tea_inventory.json", "w") as f:
        json.dump(new_inv, f, indent=2)
    
    return new_inv



  

    
def order_items(dict):
    working_dir = os.getcwd()
    ignore = [
        "NA",
        "?"
    ]
    for item in dict:
        print(item["ordered_amount"])
        order_quatity = int(item["ordered_amount"] / 16)
        if order_quatity >= 1:
            url = item["url"]
            if url not in ignore:
                driver = webdriver.Firefox(executable_path=fr"{working_dir}/geckodriver")
                add_to_cart_xpath = """//*[@id="add-to-cart-button"]"""
                for i in range(order_quatity):

                    loaded = False
                    driver.get(url)
                    while loaded != True:
                        failed = False
                        try:
                            #time.sleep(3)
                            count =0 
                            
                            driver.find_element_by_css_selector(".a-icon-radio-inactive").click()                  
                            driver.find_element_by_xpath("""//*[@id="add-to-cart-button"]""").click()
                            break
                        except:
                            failed = True
                            print("ERROR!!")
                        if failed != True:
                            loaded = True
                            break
                subtract = order_quatity*16
                item["ordered_amount"] = item["ordered_amount"] - subtract
    with open("tea_inventory.json", "w") as f:
        json.dump(dict, f, indent=2)
    def login(text, passwd):
        text_input = driver.find_element_by_id("ap_email")
        text_input.send_keys(text)
        text_input.send_keys(Keys.ENTER)
        pass_input = driver.find_element_by_id("PasswordInputManagers")
        pass_input.send_keys(passwd)
        pass_input.send_keys(Keys.ENTER)

if False:
    def create_worksheet(data):
        with open(f"{data}", "r") as f:
            df = pd.json_normalize(json.load(f))
            df.to_excel("tea_worksheet.xlsx")


