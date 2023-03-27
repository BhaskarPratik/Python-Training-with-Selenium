from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=serv_obj, options=chrome_option)
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/search?q=apple")

# search_box = driver.find_element(By.XPATH,"//input[@id='q']")
# search_box.clear()
# search_box.send_keys("Apple MacBook Pro 13-inch")
#
# print("Result of text : ", search_box.text) # printed nothing
# print("Result of get_attribute : ", search_box.get_attribute('value'))  # Apple MacBook Pro 13-inch

btn = driver.find_element(By.XPATH,"//button[@class='button-1 search-button']")
print("result of text : ", btn.text)  # SEARCH
print("result of get_attribute : ", btn.get_attribute('value'))  #  printed nothing
print("result of get_attribute : ", btn.get_attribute('type'))  # submit

driver.quit()