import time
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle


options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

driver.get("https://garmsaffiliated.com/en-us/collections/garms")

# #print(driver.get_cookies())  #get_cookie -- можна вибрати певні кукі які будуть діставатись
#
# driver.add_cookie({
#     "name" : "NiceCock",
#     "value" : "meow"
# })
#
# before_changes = driver.get_cookie("cart_currency")
# print(before_changes)
#
# driver.delete_cookie("cart_currency")
#
#
# driver.add_cookie({
#     "name" : "cart_currency",
#     "value" : "USDT"
# })
#
# after_changes = driver.get_cookie("cart_currency")
#
# print(after_changes)


driver.delete_all_cookies()

#pickle.dump(driver.get_cookies(), open(os.getcwd()+"/cookies/all_cookes.pkl", "wb"))

cookies = pickle.load(open(os.getcwd()+"/cookies/all_cookes.pkl", "rb"))

for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()