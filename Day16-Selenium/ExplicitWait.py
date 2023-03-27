from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=serv_obj, options=chrome_option)

# my_wait = WebDriverWait(driver, 10,) # basic syntax
my_wait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[
    NoSuchElementException,
    ElementNotVisibleException,
    ElementNotSelectableException,
    Exception
])

driver.get("https://www.google.com")
driver.maximize_window()

search_box = driver.find_element(By.XPATH, "//input[@name='q']")
search_box.send_keys("Selenium")
search_box.submit()

search_link = my_wait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Selenium']")))
search_link.click()

driver.quit()
