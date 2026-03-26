import os
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory" : f"{os.getcwd()}/downl",
    "safebrowsing.enabled" : True,
    "download.prompt_for_download" : False,
    "download.directory_upgrade": True

}

chrome_options.page_load_strategy = "eager"
#chrome_options.add_argument("--incognito")
chrome_options.add_experimental_option("prefs", prefs)
service = Service(executable_path= ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options = chrome_options)

driver.get("https://the-internet.herokuapp.com/download")


file = driver.find_elements("xpath", "//a")[3]

actions = ActionChains(driver)
actions.move_to_element(file).perform()

file.click()

time.sleep(5)
