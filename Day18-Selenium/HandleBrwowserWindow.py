import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options, service=ser_obj)


driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

# window_id = driver.current_window_handle
# print(window_id)  # CDwindow-6FE2D2714A9FE2EA475BA1D4574DD5F6
# # CDwindow-1079525EC8FB573BCE5B952B2936952F

time.sleep(10)
driver.find_element(By.XPATH, "//div[@class='orangehrm-copyright-wrapper']/p/a").click()

# Approach 1:

window_ids = driver.window_handles
# parent_window_id = window_ids[0]
# child_window_id = window_ids[1]
#
# print("Parent Window : ",parent_window_id,"Child Window : ",child_window_id)
#
# driver.switch_to.window(parent_window_id)
# print("title of the parent window: ",driver.title)
# driver.switch_to.window(child_window_id)
# print("title of the child window: ",driver.title)

# Approach 2: looping
# for winid in window_ids:
#     driver.switch_to.window(winid)
#     print(driver.title)


# close specific browser window
for winid in window_ids:
    driver.switch_to.window(winid)
    if driver.title == "OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM":
        driver.close()