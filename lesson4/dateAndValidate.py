import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://uk.wikipedia.org")

# url = driver.current_url
# print("ur url is:", url)
# assert url == "https://uk.wikipedia.org/wiki/%D0%93%D0%BE%D0%BB%D0%BE%D0%B2%D0%BD%D0%B0_%D1%81%D1%82%D0%BE%D1%80%D1%96%D0%BD%D0%BA%D0%B0" , "error not your url"
#
# my_title = driver.title
# print("ur title is:", my_title)
# assert my_title == "Вікіпедія" , "ny i dayn"

print(driver.page_source)
time.sleep(5)