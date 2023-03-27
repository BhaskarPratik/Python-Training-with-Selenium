from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj_serv = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=obj_serv, options=chrome_options)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()  # Maximize the browser window

# name and id locators
# driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver.find_element(By.NAME,"q").send_keys("Lenovo Thinkpad X1 Carbon Laptop")

# linkText and partialLinkText locators
# driver.find_element(By.LINK_TEXT,"Register").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"ster").click()
