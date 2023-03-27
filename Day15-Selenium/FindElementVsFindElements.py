from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=serv_obj, options=chrome_option)
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/")

# find_element() --> return single web-element

# 1) Locator matching with single web-element
# obj_element = driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# obj_element.send_keys("Apple MacBook Pro 13-inch")

# 2) Locator matching with multiple web-element
# obj_element = driver.find_element(By.XPATH,"//div[@class='footer']//a")
# print(obj_element.text)

# 3) element not available then throw NoSuchElementException  -->  unable to locate element
# login_element = driver.find_element(By.LINK_TEXT,"Log")
# login_element.click()  # NoSuchElementException: Message: no such element: Unable to locate element:


# find_elements() --> return multiple web-elements  ---> return the web-element & web-elements in the form of  list
# 1) Locator matching with single web-element
# obj_elements = driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
# print(len(obj_elements))
# obj_elements[0].send_keys("Apple MacBook Pro 13-inch")

# 2) Locator matching with multiple web-element
# obj_elements = driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# print(len(obj_elements)) # 23
# print(obj_elements[0].text)  # Sitemap
#
# for i in obj_elements:
#     print(i.text)


# 3) element not available  -- zero will be return
login_elements = driver.find_elements(By.LINK_TEXT,"Log")
print(len("Elements Returned",login_elements))

driver.quit()
