# we need to install request package through file ---> setting-->Python Interpreter
import requests as req
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

s_obj = Service('C:\Drivers\chromedriver_win32\chromedriver.exe')
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=s_obj, options=chrome_option)

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

all_links = driver.find_elements(By.TAG_NAME, "a")
count = 0

for link in all_links:
    url = link.get_attribute('href')
    try:
        res = req.head(url)
    except:
        None

    if res.status_code >= 400:
        print(url, " is broken link")
        count += 1
    else:
        print(url, " is valid link")
print(" Total number of broken links: ", count)

driver.quit()
