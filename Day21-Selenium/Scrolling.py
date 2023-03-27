import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ser_obj, options=chrome_option)
driver.implicitly_wait(10)

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window()

# 1. scroll down page by pixel
# driver.execute_script("window.scrollBy(0,3000)","")
# value = driver.execute_script("return window.pageYOffset;")
# print("No of pixel moved : ", value) # 3000

# 2. scroll down page till the element is visible
# flag = driver.find_element(By.XPATH,"//img[@alt='Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# value = driver.execute_script("return window.pageYOffset;")
# print("No of pixel moved : ", value)

# 3. scroll down page till the end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value = driver.execute_script("return window.pageYOffset;")
print("No of pixel moved : ", value)

time.sleep(5)
# scroll up to starting position
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)") # 0
