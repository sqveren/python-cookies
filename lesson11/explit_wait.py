from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
service = Service(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10, 1)


#driver.get("https://demoqa.com/dynamic-properties")

# ENABLE_BUTTON = ("xpath", "//button[@id='enableAfter']")
# #VISIBLE_AFTER_BUTTON = ("xpath", "//button[@id='visibleAfter']") #кортеж який потім буде розпакований
#
# #button1 = wait.until(EC.visibility_of_element_located(VISIBLE_AFTER_BUTTON)) # автоматичне розпакування кортежа без *
# button1 = wait.until(EC.element_to_be_clickable(ENABLE_BUTTON))
#
# button1.click()

#------------

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

VANISH_BUTTON = ("xpath", "//button[text() = 'Remove']")

button_vanish = driver.find_element(*VANISH_BUTTON)
button_vanish.click()

wait.until(EC.invisibility_of_element_located(VANISH_BUTTON))

print("пропала дура")
