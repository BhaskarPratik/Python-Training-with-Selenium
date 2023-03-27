from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options, service=ser_obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

# 1) count no of rows and columns
no_of_rows = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))
print(no_of_rows)

no_of_columns = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr/th"))
print(no_of_columns)

# 2) read specific row and column data

# data = driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[1]").text
# print(data) # Master In Selenium

# 3) Read all the rows and column data
# print("Print all the rows and column data")
# for r in range(2, no_of_rows + 1):
#     for c in range(1, no_of_columns + 1):
#         data = driver.find_element(By.XPATH,
#                                    "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
#         print(data, end="  ")
#     print()

# 4) Read data based on condition (list book name whose author is mukesh)
for r in range(2, no_of_rows + 1):
    author = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[2]").text
    if author == "Mukesh":
        book_name = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[1]").text
        price = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[4]").text
        print(book_name, " ",  author, " ", price)
driver.close()
