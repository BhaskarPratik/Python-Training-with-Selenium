import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ser_obj, options=chrome_options)

driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

f1 = driver.find_element(By.XPATH, "//input[@id='field1']")
f1.clear()
f1.send_keys("Amar")
btn = driver.find_element(By.XPATH, "//button[.='Copy Text']")
act = ActionChains(driver)

act.double_click(btn).perform()

source = driver.find_element(By.XPATH, "//div[@id='draggable']")
target = driver.find_element(By.XPATH, "//div[@id='droppable']")

act.drag_and_drop(source, target).perform()

src1 = driver.find_element(By.XPATH, "//img[@alt='the peaks of high tatras']")
src2 = driver.find_element(By.XPATH, "//img[@alt='The chalet at the Green mountain lake']")

target1 = driver.find_element(By.XPATH, "//div[@id = 'trash']")

act.drag_and_drop(src1, target1).perform()
act.drag_and_drop(src2, target1).perform()

slider_btn = driver.find_element(By.XPATH, "//*[@id='slider']/span")
print(slider_btn.location)

time.sleep(5)
act.drag_and_drop_by_offset(slider_btn, 540, 0).perform()
