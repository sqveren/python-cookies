import pickle
import os
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_argument("--lang=en-GB")
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 20, 1)


driver.get("https://www.amazon.com/Muddy-Mats-Premium-Absorbent-Chenille/dp/B08N6VLJKV?ref=dlx_bigsp_dg_dcl_B08N6VLJKV_dt_sl5_2f_pi&pf_rd_r=M851ZBRBB3NYBJY99DJG&pf_rd_p=4b6db39a-ff31-4e8d-be21-a5a17afac12f")

ADD_TO_CARD_BUTTON = ("xpath", "//input[@id = 'add-to-cart-button']")

#add_to_card_button = driver.find_element(*ADD_TO_CARD_BUTTON)

driver.delete_cookie("sp-cdn")
driver.add_cookie({
    "name": "sp-cdn",
    "value": "L5Z9:GB"
})

cart_btn = wait.until(EC.visibility_of_element_located(ADD_TO_CARD_BUTTON))
cart_btn.click()

pickle.dump(driver.get_cookies(), open(os.getcwd()+"/cookies/amazon_cookies.pkl","wb"))

driver.refresh()
time.sleep(10)
driver.delete_all_cookies()

cookies = pickle.load(open(os.getcwd()+"/cookies/amazon_cookies.pkl","rb"))

for cookie in cookies:
    driver.add_cookie(cookie)

driver.refresh()

time.sleep(10)
