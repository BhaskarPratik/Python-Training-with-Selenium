from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=ser_obj,options=chrome_option)

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.switch_to.frame(0)
# driver.find_element(By.XPATH,"//input[@id = 'datepicker']").send_keys("02/27/2023")

year = "2021"
month = "May"
date = "18"

driver.find_element(By.XPATH,"//input[@id = 'datepicker']").click()

while True:
    mon = driver.find_element(By.XPATH, "//span[@class = 'ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class = 'ui-datepicker-year']").text

    if mon == month and yr == year:
        break
    else:
        # driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click() # nxt arrow
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click() # previous arrow

# select date
dates = driver.find_elements(By.XPATH,"//table[@class = 'ui-datepicker-calendar']/tbody/tr/td/a")
for ele in dates:
    if ele.text == date:
        ele.click()
        break
