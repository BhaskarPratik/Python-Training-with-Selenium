from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=serv_obj, options=chrome_option)
driver.get("https://www.facebook.com/")
driver.maximize_window()

# tag and id
# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("abc")
# driver.find_element(By.CSS_SELECTOR, "#email").send_keys("abc")  # tag name is optional

# tag and class
# driver.find_element(By.CSS_SELECTOR,'input.inputtext').send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR,'.inputtext').send_keys("abc@gmail.com") # tag name is optional

# tag and attribute
# driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR,"input[name= email]").send_keys("abc@gmail.com")
# driver.find_element(By.CSS_SELECTOR,"[data-testid=royal_email]").send_keys("abc@gmail.com")

# tag class and attribute
driver.find_element(By.CSS_SELECTOR,"input.inputtext[name=pass]").send_keys("9839989796")

