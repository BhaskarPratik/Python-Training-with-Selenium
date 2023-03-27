from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=serv_obj, options=chrome_option)
driver.implicitly_wait(10)

driver.get("https://www.google.com")
driver.maximize_window()

search_box = driver.find_element(By.XPATH,"//input[@name='q']")
search_box.send_keys("Selenium")
search_box.submit()

driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()
driver.quit()
