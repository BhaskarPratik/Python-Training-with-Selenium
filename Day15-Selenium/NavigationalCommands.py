from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=serv_obj, options=chrome_option)
driver.maximize_window()
driver.get("https://www.snapdeal.com/")
driver.get("https://www.amazon.in/")
driver.back() # snap-deal
driver.forward()  # amazon
driver.refresh()
driver.quit()