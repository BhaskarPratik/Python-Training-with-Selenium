import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options, service=ser_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# Example 1: close and accept alert

# driver.find_element(By.XPATH, "//button[contains(normalize-space(),'Click Me')]").click()
# my_alert = driver.switch_to.alert
# # my_alert.accept() # accept alert
# my_alert.dismiss() # close alert

driver.find_element(By.XPATH, "//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("selenium")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@class='wikipedia-search-button']").click()

time.sleep(5)
serch_result_links = driver.find_elements(By.XPATH, "//div[@id='wikipedia-search-result-link']/a")

for links in serch_result_links:
    links.click()

window_ids = driver.window_handles

for winid in window_ids:
    driver.switch_to.window(winid)
    print(driver.title)
    if driver.title == "Automation Testing Practice" or "Selenium disulfide - Wikipedia" or "Selenium (software) - Wikipedia" or "Selenium - Wikipedia" or "Selenium in biology - Wikipedia" or "Selenium dioxide - Wikipedia":
        driver.close()
driver.quit()
