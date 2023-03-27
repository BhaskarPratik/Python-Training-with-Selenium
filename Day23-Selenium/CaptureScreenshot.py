from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os

ser_obj = Service("E:\Drivers\chromedriver_win32\chromedriver.exe")
opt = Options()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ser_obj, options=opt)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

# driver.save_screenshot("E:\\PythonTraining\\Day23-Selenium\\homepage.png")
# driver.save_screenshot(os.getcwd() + "\\demopage.png")


driver.get_screenshot_as_file(os.getcwd() + "\\landing_page.png")

# driver.get_screenshot_as_base64() driver.get_screenshot_as_png()  ==> save in binary format
driver.quit()
