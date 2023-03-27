from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

obj_ser = Service('C:\Drivers\chromedriver_win32\chromedriver.exe')
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=obj_ser, options=chrome_option)

driver.get("https://money.rediff.com/losers/bse/daily/groupa")
driver.maximize_window()

# self
# txtMsg = driver.find_element(By.XPATH, "//a[contains(text(),'India Glycols')]/self::a").text
# print(txtMsg)

# parent
# txtMsg = driver.find_element(By.XPATH,"//a[contains(text(),'India Glycols')]/parent::td").text
# print(txtMsg)

# child

# child = driver.find_elements(By.XPATH,"//a[contains(text(),'India Glycols')]/ancestor::tr/child::td")
# print(len(child))

# for i in child:
#     print(i.text)

# ancestor
# txtMsg = driver.find_element(By.XPATH,"//a[contains(text(),'India Glycols')]/ancestor::tr").text
# print(txtMsg)

# descendant

# descendants = driver.find_elements(By.XPATH,"//a[contains(text(),'India Glycols')]/ancestor::tr/descendant::*")
# print(len(descendants))

# for i in descendants:
#     print(i.text)

# following

# following = driver.find_elements(By.XPATH,"//a[contains(text(),'India Glycols')]/ancestor::tr/following::*")
# print(len(following)) # 2450


# following siblings

# following_siblings = driver.find_elements(By.XPATH,"//a[contains(text(),'India Glycols')]/ancestor::tr/following-sibling::*")
# print(len(following_siblings)) # 285

# preceding

# preceding = driver.find_elements(By.XPATH, "//a[contains(text(),'India Glycols')]/ancestor::tr/preceding::*")
# print(len(preceding))  # 475

# preceding-siblings
preceding_siblings = driver.find_elements(By.XPATH, "//a[contains(text(),'India Glycols')]/ancestor::tr/preceding-sibling::*")
print(len(preceding_siblings))  # 34

driver.close()
