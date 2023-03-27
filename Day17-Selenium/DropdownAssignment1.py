from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option, service=ser_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

ddl_speed = Select(driver.find_element(By.XPATH, "//select[@id='speed']"))
# ddl_speed.select_by_visible_text("Fast")
# ddl_speed.select_by_index(1)  # slow


# capture all the option and print them
all_options = ddl_speed.options
# print(len(all_options))
#
# for options in all_options:
#     print(options.text)

# select option from the dropdown without using built in method
for opt in all_options:
    if opt.text == "Slow":
        opt.click()
        break

