import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=s_obj, options=chrome_option)

driver.get("https://itera-qa.azurewebsites.net/home/automation")
driver.maximize_window()

# 1) select specific checkbox
# driver.find_element(By.XPATH,"//input[@id='monday']").click()

# 2) select all the checkboxes
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkboxes))  # 7

# Approach 1: using for loop with range function
# for i in range(len(checkboxes)):
#     print(i)
#     checkboxes[i].click()

# Approach 2: using for loop only
for checkbox in checkboxes:
    # print(checkbox)
    checkbox.click()


# 3)  select multiple checkboxes by choice
# for checkbox in checkboxes:
#     week_name = checkbox.get_attribute('id')
#     if week_name == 'monday' or week_name == 'sunday':
#         checkbox.click()

# 4)  select last 2 checkboxes from the last
# for i in range(len(checkboxes) - 2, len(checkboxes)):
#     checkboxes[i].click()

# 5)  select first 2 checkboxes
# for i in range(len(checkboxes)):
#     if i < 2:
#         checkboxes[i].click()

# 6) clearing all the checkbox
time.sleep(5)
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
