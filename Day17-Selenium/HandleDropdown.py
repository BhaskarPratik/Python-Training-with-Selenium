import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ser_obj, options=chrome_option)
driver.get("https://www.opencart.com/index.php?route=account/register")

driver.maximize_window()

drp_country = Select(driver.find_element(By.XPATH, "//select[@id = 'input-country']"))

# select option from the dropdown
# drp_country.select_by_visible_text("India") # India
# drp_country.select_by_index(3) # Algeria
# drp_country.select_by_value("4")  # American Samoa

# capture all the option and print them

all_options = drp_country.options
# print("Print all the option : ", len(all_options))

# for opt in all_options:
#     print(opt.text)

# select option from the dropdown without using built in method
for opt in all_options:
    if opt.text == "India":
        opt.click()
        break

# ddl_options = driver.find_elements(By.XPATH, "//select[@id = 'input-country']/option")
# print("Dropdown options ",len(ddl_options))
