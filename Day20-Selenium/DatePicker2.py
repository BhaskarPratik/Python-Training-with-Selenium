import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=ser_obj,options=chrome_option)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='dob']").click()  # opens date picker

months = Select( driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']"))
months.select_by_visible_text("Aug")

year = Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']"))
year.select_by_visible_text("2020")

all_dates = driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")

for date in all_dates:
    if date.text == "26":
        date.click()
        break