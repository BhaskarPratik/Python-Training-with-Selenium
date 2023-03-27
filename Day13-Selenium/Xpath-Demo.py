from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service_obj =Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach",True)
driver = webdriver.Chrome(service= service_obj, options=chrome_option)


driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# Absolute xpath
# driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[2]/form/input").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver.find_element(By.XPATH,"/html/body/div[6]/div[1]/div[2]/div[2]/form/button").click()

# Relative xpath
# driver.find_element(By.XPATH,'//*[@id="small-searchterms"]').send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver.find_element(By.XPATH,'//*[@id="small-search-box-form"]/button').click()

# or and
# driver.find_element(By.XPATH,"//input[@id='small-searchterms' or @placeholder='Search store']").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver.find_element(By.XPATH,"//button[@type='submit' and @class='button-1 search-box-button']").click()

# contains() startwith()
# driver.find_element(By.XPATH,"//input[contains(@placeholder,'Search ')]").send_keys("Lenovo Thinkpad X1 Carbon Laptop")
# driver.find_element(By.XPATH,"//button[starts-with(@type,'sub')]").click()

# text()
driver.find_element(By.XPATH,"//button[text()='Search']").click()



