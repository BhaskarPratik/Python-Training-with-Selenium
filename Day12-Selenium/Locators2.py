from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=serv_obj, options=chrome_option)

driver.get("https://www.theshilpashetty.com/")
driver.maximize_window()

sliders = driver.find_elements(By.CLASS_NAME, "bg")
print(len(sliders))  # 15 total no of sliders on home page

links= driver.find_elements(By.TAG_NAME, "a")
print(len(links)) # 56 total no of links
