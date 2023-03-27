from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

from selenium.webdriver.common.by import By

ser_obj = Service("E:\Drivers\chromedriver_win32\chromedriver.exe")
opt = Options()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ser_obj, options=opt)

# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# driver.find_element(By.LINK_TEXT,"Register").send_keys(Keys.CONTROL + Keys.RETURN)

# # New tab = selenium 4: open a new tab and switches to a new tab
# driver.get("https://www.opencart.com/")
# driver.switch_to.new_window('tab')
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# New tab = selenium 4: open a new browser windows  and switches to a new window
driver.get("https://www.opencart.com/")
driver.switch_to.new_window('window')
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")