from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

ser_obj = Service("E:\Drivers\chromedriver_win32\chromedriver.exe")
opt = Options()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ser_obj, options=opt)

driver.get("https://www.foundit.in/employment-index/")
driver.maximize_window()

driver.find_element(By.XPATH, "//*[@id='heroSection-container']/div[3]/div[2]").click()
driver.find_element(By.XPATH, "//input[@id='file-upload']").send_keys("E:\\JoytiDocs\\uancard.pdf")