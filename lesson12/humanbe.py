from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--window-size=1920,1920")
chrome_options.add_argument("--disabled_blink-features=AutomationControlled") #не достатньо щоб здаватись людиною але теж потрібне
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36")
#тепер сайт думає що ми людина і зазвичай не має видавати перевірку на людину навіть в хедлесс моді
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

service = Service(executable_path = ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options = chrome_options)
wait = WebDriverWait(driver, 10, 1)


driver.get("https://garmsaffiliated.com/en-us/collections/garms")

driver.save_screenshot("scren.png")
wait.until(EC.title_contains("Garms"))

