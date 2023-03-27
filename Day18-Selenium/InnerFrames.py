from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options, service=ser_obj)

driver.get("https://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.LINK_TEXT, "Iframe with in an Iframe").click()

outer_frame = driver.find_element(By.XPATH, "//div[@id='Multiple']/iframe")
driver.switch_to.frame(outer_frame)

inner_frame = driver.find_element(By.XPATH, "//div[@class='iframe-container']/iframe")
driver.switch_to.frame(inner_frame)

driver.find_element(By.XPATH, "//input[@type='text']").send_keys("welcome")
driver.switch_to.parent_frame()  # directly switch to parent frame(outer frame)
