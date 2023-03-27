from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ser_obj, options=chrome_option)
driver.implicitly_wait(10)

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()

driver.switch_to.frame(0)
f1 = driver.find_element(By.XPATH, "//input[@id='field1']")
f1.clear()
f1.send_keys("Rahul")

btn = driver.find_element(By.XPATH, "//button[contains(.,'Copy Text')]")

act = ActionChains(driver)
act.double_click(btn).perform()  # double click action
