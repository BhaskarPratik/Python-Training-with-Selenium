import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=ser_obj,options=chrome_option)

driver.get("https://bootstrapmade.com/")
driver.maximize_window()

# Mouse_Hover
templates  = driver.find_element(By.XPATH,"//span[.='Templates']")
real_estate = driver.find_element(By.XPATH,"//a[.='Real Estate']")
act = ActionChains(driver)
act.move_to_element(templates).move_to_element(real_estate).click().perform()