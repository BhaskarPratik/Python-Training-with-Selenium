from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

ser_obj = Service("E:\Drivers\chromedriver_win32\chromedriver.exe")
opt = Options()
opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ser_obj, options=opt)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()

cookies = driver.get_cookies()
print("length of cookies :", len(cookies))  # 3

# for c in cookies:
#     print(c)
#     print(c.get('name'))
#     print(c.get('name',":"),c.get('value'))

# add new cookies in the browser
driver.add_cookie({"name": "MyCookie", "value": "123456"})
cookies = driver.get_cookies()
print("size of cookies after adding new cookies : ", len(cookies))  # 4

# delete the specific cookies from the browser
driver.delete_cookie("MyCookie")
cookies = driver.get_cookies()
print("size of cookies after deleted one:", len(cookies))  # 3

# delete all the cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print("size of deleting all cookies : ", cookies) # []
driver.quit()
