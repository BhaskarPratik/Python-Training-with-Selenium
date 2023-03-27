import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option, service=ser_obj)

driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Click for JS Prompt')]").click()
alert_popup = driver.switch_to.alert
print(alert_popup.text)
alert_popup.send_keys("Python")
time.sleep(5)
# alert_popup.accept()  # accept through the ok button
alert_popup.dismiss()  # cancel through the dismiss button
