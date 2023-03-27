from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

ser_obj = Service("E:\Drivers\chromedriver_win32\chromedriver.exe")
opt = Options()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ser_obj, options=opt)
driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

driver.find_element(By.XPATH, "//span[@id='select2-billing_country-container']").click()
countries_list = driver.find_elements(By.XPATH, "//*[@id='select2-billing_country-results']/li")
print(len(countries_list))

for country in countries_list:
    if country.text == 'Jordan':
        country.click()
        break
