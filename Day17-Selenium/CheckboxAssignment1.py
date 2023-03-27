import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option, service=ser_obj)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# 1) select specific checkbox
# driver.find_element(By.XPATH,"//input[@id='monday']").click()

# 2) select all the checkboxes
all_checkbox = driver.find_elements(By.XPATH,
                                    "//input[@type = 'checkbox']/ancestor::div[@class = 'form-check']/label/input")

print(len(all_checkbox))

# Approach 1 :

# for i in range(len(all_checkbox)):
#     all_checkbox[i].click()

# Approach 2:
# for checkboxes in all_checkbox:
#     checkboxes.click()

# 3)  select multiple checkboxes by choice

for day_checkbox in all_checkbox:
    week_name = day_checkbox.get_attribute('id')
    if week_name == 'sunday' or week_name == 'wednesday':
        day_checkbox.click()





