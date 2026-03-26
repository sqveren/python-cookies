from selenium.webdriver import ActionChains
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://garmsaffiliated.com/en-us/collections/garms")

parent_menu = driver.find_element("xpath", "(//hover-disclosure[contains(@class, 'menu__item')])[3]")

# 2. Наводимо мишку і клікаємо на посилання всередині
actions = ActionChains(driver)
actions.move_to_element(parent_menu).perform() # Навели курсор

# 3. Тепер клікаємо по самому посиланню
link = parent_menu.find_element("xpath", ".//a[contains(@class, 'navlink')]")
link.click()

login_field = driver.find_element("xpath", "//input[contains(@id, 'Form-template--28898864988505__contact-0')]")
login_field.send_keys("sqveren@gmail.com")
print(login_field.get_attribute("value"))

login_field.clear()

login_field.send_keys("ny tu lox")

time.sleep(5)
