import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options, service=ser_obj)

driver.get("https://mypage.rediff.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@value=' Go ']").click()
time.sleep(5)
driver.switch_to.alert.accept()

