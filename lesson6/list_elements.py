import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("https://garmsaffiliated.com/en-us/collections/garms")

driver.find_elements("class name","menu__item  child")[2].click()

time.sleep(10)

