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

# login
time.sleep(5)
driver.find_element(By.XPATH, "//input[@name = 'username']").send_keys("Admin")
driver.find_element(By.XPATH, "//input[@name = 'password']").send_keys("admin123")
driver.find_element(By.XPATH, "//button[@class= 'oxd-button oxd-button--medium oxd-button--main "
                              "orangehrm-login-button\']").click()

# admin --> user_management --> user
time.sleep(5)
driver.find_element(By.XPATH, "//ul[@class= 'oxd-main-menu']/li/a[contains(.,'Admin')]").click()
time.sleep(5)
driver.find_element(By.XPATH, "//nav//span[contains(.,'User Management ')]").click()
driver.find_element(By.XPATH, "//ul//a[contains(.,'Users')]").click()

# total no of rows
time.sleep(5)
rows = len(driver.find_elements(By.XPATH,
                                "//div[@class='oxd-table-card']/div[@class='oxd-table-row oxd-table-row--with-border']"))
print("Print length of the rows: ", rows)

count = 0
for r in range(1, rows + 1):
    status = driver.find_element(By.XPATH,
                                 "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[" + str(
                                     r) + "]//div[5]").text
    if status == "Enabled":
        count = count + 1
print("Total no of user : ", rows)
print("Total no of enabled user : ", count)
print("Total no of disabled user : ", (rows-count))

driver.close()
