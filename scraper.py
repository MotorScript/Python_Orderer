from selenium import webdriver
import os



def click_button(xpath):
    loaded = False
    while loaded != True:
        failed = False
        try:
            driver.find_element_by_xpath(xpath).click()
        except:
            failed = True
            print("ERROR!!")
        if failed != True:
            loaded = True
            break

working_dir = os.getcwd()


driver = webdriver.Firefox(executable_path=fr"{working_dir}/geckodriver")

url = "https://www.amazon.com/gp/css/homepage.html?ref_=nav_youraccount_switchacct&"
