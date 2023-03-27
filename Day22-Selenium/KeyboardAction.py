import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

ser_obj = Service("E:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ser_obj, options=chrome_option)
driver.implicitly_wait(10)

driver.get("https://text-compare.com/")
driver.maximize_window()

input1 = driver.find_element(By.XPATH, "//textarea[@id= 'inputText1']")
input2 = driver.find_element(By.XPATH, "//textarea[@id= 'inputText2']")

input1.send_keys("Welcome to selenium")

act = ActionChains(driver)

# input 1 ===> ctrl + A select the text
act.key_down(Keys.CONTROL)
act.send_keys("a")
act.key_up(Keys.CONTROL)
act.perform()

# act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()

# input 1 ===> ctrl + C copy the text
act.key_down(Keys.CONTROL)
act.send_keys("c")
act.key_up(Keys.CONTROL)
act.perform()

# act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()

# press tab key navigate to input 2
act.send_keys(Keys.TAB).perform()

# input 2  ===> ctrl + v
act.key_down(Keys.CONTROL)
act.send_keys("v")
act.key_up(Keys.CONTROL)
act.perform()

# act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
