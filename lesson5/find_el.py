import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains

service = Service(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://garmsaffiliated.com/en-us/collections/garms")

element = driver.find_element("id", "product-item--template--28898864660825__main-15388092727641")

driver.execute_script("arguments[0].scrollIntoView(true);", element)

actions = ActionChains(driver)
actions.move_to_element(element).click().perform()
time.sleep(5)