from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=serv_obj, options=chrome_option)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# is_displayed(), is_enabled()
search_box = driver.find_element(By.XPATH, "//input[@id='small-searchterms']")
print("Enable Status: ", search_box.is_enabled())
print("Display Status: ", search_box.is_displayed())

# is_selected   --> for radio btn and checkboxes
driver.find_element(By.XPATH, "//a[contains(text(),'Register')]").click()

rd_male = driver.find_element(By.XPATH, "//input[@id='gender-male']")
rd_female = driver.find_element(By.XPATH, "//input[@id='gender-female']")

print("By default status of radio btn : ")
print(rd_male.is_selected())  # False
print(rd_female.is_selected())  # False


rd_male.click()  # select male radio btn

print("After male radio btn selected : ")
print(rd_male.is_selected())  # True
print(rd_female.is_selected()) # False

rd_female.click() # select female radio btn

print("After female radio btn selected : ")
print(rd_male.is_selected())  # False
print(rd_female.is_selected()) # True

driver.close()
