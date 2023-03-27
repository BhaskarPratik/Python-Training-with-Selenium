from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach",True)
driver = webdriver.Chrome(options=chrome_option,service=ser_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

ddl_Product  = Select(driver.find_element(By.XPATH,"//select[@id = 'products']"))
# ddl_Product.select_by_index(3) # bing
# ddl_Product.select_by_visible_text("Yahoo")  # Yahoo
# ddl_Product.select_by_value("Microsoft")  # bing

# capture all the option and print them
all_products = ddl_Product.options
# print(len(all_products))
#
# for product in all_products:
#     print(product.text)

# select option from the dropdown without using built in method
for product in all_products:
    if product.text == "Yahoo":
        product.click()
        break


