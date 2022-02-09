import click
from selenium import webdriver
import os
import time
from selenium.webdriver.common.keys import Keys
import json


working_dir = os.getcwd()
driver = webdriver.Firefox(executable_path=fr"{working_dir}/geckodriver")

class scraper:
    def __init__(self, url_list):
        self.url_list = url_list
    

    
    def order_items(self):
        with open(self.url_list, "r") as f:
            urls = json.load(f)
        for i in urls:

            add_to_cart_xpath = """//*[@id="add-to-cart-button"]"""

            loaded = False

            driver.get(i)
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

    def login(text, passwd):
        text_input = driver.find_element_by_id("ap_email")
        text_input.send_keys(text)
        text_input.send_keys(Keys.ENTER)
        pass_input = driver.find_element_by_id("PasswordInputManagers")
        pass_input.send_keys(passwd)
        pass_input.send_keys(Keys.ENTER)
        

    #login("countrytexasboys@gmail.com", "Bornfree1611")
    #driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
