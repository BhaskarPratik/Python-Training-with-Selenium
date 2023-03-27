import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

s_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=s_obj, options=chrome_option)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Click on link
# driver.find_element(By.PARTIAL_LINK_TEXT, "Digital").click()
# driver.find_element(By.LINK_TEXT,"Digital downloads ").click()

# find no of links in a page
links = driver.find_elements(By.XPATH,"//a")
print("Total no of links: ",len(links))

# print all the link names
for link in links:
    print(link.text)


driver.quit()