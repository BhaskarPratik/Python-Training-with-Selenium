from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach",True)
driver = webdriver.Chrome(service= serv_obj,options=chrome_option)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
print(driver.title) # OrangeHRM
print(driver.current_url) # https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
print(driver.page_source)
driver.close()