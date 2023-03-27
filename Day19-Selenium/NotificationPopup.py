from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach",True)
chrome_option.add_argument("--disable-notification")
driver = webdriver.Chrome(service= ser_obj,options=chrome_option)
driver.get("https://whatmylocation.com/")
driver.maximize_window()
