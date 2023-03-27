import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

ser_obj =  Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_options = Options()
chrome_options.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_options,service=ser_obj)

driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")
driver.maximize_window()

driver.switch_to.frame("packageListFrame")

driver.find_element(By.LINK_TEXT,"org.openqa.selenium").click()

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")

driver.find_element(By.LINK_TEXT,"WebDriver").click()

driver.switch_to.default_content()

driver.switch_to.frame("classFrame")

driver.find_element(By.XPATH,"//div[@class='topNav']/ul[@class='navList']/li/a[contains(text(),'Help')]").click()