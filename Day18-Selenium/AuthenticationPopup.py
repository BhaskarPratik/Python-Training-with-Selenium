from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_option,service=ser_obj)
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/basic_auth")
driver.get("https://admin:admin@the-internet.herokuapp.com/basic_auth")