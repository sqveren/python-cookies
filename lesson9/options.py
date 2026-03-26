from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

chromeOptions = webdriver.ChromeOptions()
chromeOptions.page_load_strategy = "eager"
#chromeOptions.add_argument("--headless")
chromeOptions.add_argument("--incognito")
#chromeOptions.add_argument("--ignore-sertificate-errors")
#chromeOptions.add_argument("--window-size=700,700")
#chromeOptions.add_argument("--disable-cache")
service = Service(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chromeOptions)


driver.set_window_size(700, 1000)

driver.get("https://garmsaffiliated.com/en-us/collections/garms")

time.sleep(3)