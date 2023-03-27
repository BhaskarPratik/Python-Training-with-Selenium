# TestCase
# 1)Open web browser(chrome / firefox / edge)
# 2)open url("https://opensource-demo.orangehrmlive.com")
# 3)Enter Username(Admin)
# 4)Enter Password (admin123)
# 5)Click on login
# 6)Capture title of the home page.(Actual Title)
# 7)Verify title of the page :Orange HRM (Expected)
# 8)Close browser

from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# obj_ser = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
# chrome_options = Options()
# chrome_options.add_experimental_option("detach",True)
# driver = webdriver.Chrome(service=obj_ser)
# driver = webdriver.Chrome(service=obj_ser,options=chrome_options)

# driver = webdriver.Chrome()
# driver.get("https://opensource-demo.orangehrmlive.com/")
# driver.implicitly_wait(10)
# driver.find_element(By.NAME, "username").send_keys("Admin")
# driver.find_element(By.NAME, "password").send_keys("admin123")
# driver.find_element(By.CLASS_NAME, "oxd-button").click()
#
# act_title = driver.title  # get title
# exp_title = "OrangeHRM"
#
# if act_title == exp_title:  # compare title
#     print("Login test passed")
# else:
#     print("Login test failed")

# https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F

driver = webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
driver.implicitly_wait(60)
driver.find_element(By.ID,"Email").clear()
driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Password").send_keys("admin")
driver.find_element(By.CLASS_NAME,"button-1 ").click()

actTitle = driver.title
expTitle  = "Dashboard / nopCommerce administration"

if actTitle == expTitle:
    print("Login Test Passed")
else:
    print("Login Test Failed")



