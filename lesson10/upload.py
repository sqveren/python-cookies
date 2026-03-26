import os
import time
from selenium.webdriver import ActionChains
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()

chrome_options.page_load_strategy = "eager"
#chrome_options.add_argument("--incognito")
#chrome_options.add_experimental_option("prefs", prefs)
service = Service(executable_path= ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options = chrome_options)

driver.get("https://the-internet.herokuapp.com/upload")
current_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "cdeec87a-50a3-48d3-8c84-4baa9f33c7c4.tmp"
file_pathh = os.path.join(current_dir,file_name)

if not os.path.exists(file_pathh):
    print(f"ПОМИЛКА: Файл не знайдено за шляхом: {file_pathh}")
    # Можна вивести список файлів у папці, щоб зрозуміти, де помилка
    print("Файли в цій директорії:", os.listdir(current_dir))
else:
    print(f"Файл знайдено! Починаю завантаження...")
    input_field = driver.find_element("xpath", "//input[@type='file']")
    input_field.send_keys(file_pathh)

input_field = driver.find_element("xpath", "//input[@type ='file']")
file_path = os.path.join(os.getcwd(),"cdeec87a-50a3-48d3-8c84-4baa9f33c7c4.tmp")






input_field.send_keys(file_path)

time.sleep(5)