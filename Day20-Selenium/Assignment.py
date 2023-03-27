import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# from selenium.webdriver.support.select import Select

ser_obj = Service("E:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ser_obj, options=chrome_option)
driver.implicitly_wait(10)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

# driver.find_element(By.XPATH, "//input[@id='travname']").send_keys("Pratik")
# driver.find_element(By.XPATH, "//input[@id='travlastname']").send_keys("Bhaskar")
#
# driver.find_element(By.XPATH, "//input[@id='dob']").click()
# mon = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
# mon.select_by_visible_text("Nov")
#
# yr = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']"))
# yr.select_by_visible_text("2008")
#
# all_dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
#
# for date in all_dates:
#     if date.text == "26":
#         date.click()
#         break
#
# driver.find_element(By.XPATH, "//*[@id='sex_1']").click()
# driver.find_element(By.XPATH, "//input[@id='fromcity']").send_keys("Mumbai")
# driver.find_element(By.XPATH, "//input[@id='tocity']").send_keys("Nashik")
#
# driver.find_element(By.XPATH, "//input[@id='departon']").click()
# mon = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-month']"))
# mon.select_by_visible_text("Jun")
#
# yr = Select(driver.find_element(By.XPATH, "//select[@class='ui-datepicker-year']"))
# yr.select_by_visible_text("2023")
#
# all_dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
# for date in all_dates:
#     if date.text == "25":
#         date.click()
#         break
#
# reasons = Select(driver.find_element(By.XPATH, "//select[@id='reasondummy']"))
# reasons.select_by_visible_text("Prank a friend")
#
# driver.find_element(By.XPATH, "//input[@id='billing_phone']").send_keys("9082747823")
# driver.find_element(By.XPATH, "//input[@id='billing_email']")
#
# country = Select(driver.find_element(By.XPATH, "//select[@id='billing_country']"))
# country.select_by_visible_text("Iran")
#
# driver.find_element(By.XPATH, "//input[@id='billing_address_1']").send_keys("Koparkhairane")
# driver.find_element(By.XPATH, "//input[@id='billing_address_2']").send_keys("Terna college")
# driver.find_element(By.XPATH, "//input[@id='billing_city']").send_keys("Navi Mumbai")
#
# state = Select(driver.find_element(By.XPATH, "//select[@id='billing_state']"))
# state.select_by_visible_text("Tehran (تهران)")
#
# driver.find_element(By.XPATH, "//input[@id='billing_postcode']").send_keys("400709")


radio_btn = driver.find_elements(By.XPATH, "//ul[@id='checkout-products']/li//input")
#
# return_ticket = driver.find_element(By.XPATH, "//*[@id='order_review']/div[1]/table/tbody/tr/td[2]/span")
# cart_subtotal = driver.find_element(By.XPATH, "//*[@id='order_review']/div[1]/table/tfoot/tr[1]/td/span")
#
product_list = driver.find_elements(By.XPATH, "//ul[@id='checkout-products']/li")
# for products in product_list:
#
#     price = driver.find_element(By.XPATH,"//*[@id='checkout-products']/li/span[2]/span")
#     radio_btn.click()
#     time.sleep(10)
#     dummy_ticket = driver.find_element(By.XPATH,"//*[@id='order_review']/div[1]/table/tbody/tr/td[2]/span")
#     return_ticket = driver.find_element(By.XPATH, "//*[@id='order_review']/div[1]/table/tbody/tr/td[2]/span")
#     cart_subtotal = driver.find_element(By.XPATH, "//*[@id='order_review']/div[1]/table/tfoot/tr[1]/td/span")
#
#     if price.text == dummy_ticket.text and price.text == return_ticket.text and price.text == cart_subtotal.text:
#         print("Price is same")
#         print("Price text:",price.text)
#         print("dummy_ticket:", dummy_ticket.text)
#         print("return_ticket:", return_ticket.text)
#         print("cart_subtotal",cart_subtotal.text)
#     else:
#         print("Price is different")

# product_list = driver.find_elements(By.XPATH, "//ul[@id='checkout-products']/li")
radio_btns = driver.find_elements(By.XPATH, "//ul[@id='checkout-products']/li//input")
# print(len(radio_btns))
# print(type(radio_btns))
#
# for plist in product_list:
#     # driver.find_element(By.XPATH, "//input[@id='product_549']").click()
#     for i in range(len(radio_btns)):
#         radio_btns[i].click()
#         time.sleep(5)
#         price = driver.find_element(By.XPATH, "//*[@id='checkout-products']/li/span[2]/span")
#         price_value = price.text
#         dummy_ticket = driver.find_element(By.XPATH, "//*[@id='order_review']/div[1]/table/tbody/tr/td[2]/span")
#         return_ticket = driver.find_element(By.XPATH, "//*[@id='order_review']/div[1]/table/tbody/tr/td[2]/span")
#         cart_subtotal = driver.find_element(By.XPATH, "//*[@id='order_review']/div[1]/table/tfoot/tr[1]/td/span")
#         if price_value == dummy_ticket.text and price_value == return_ticket.text and price_value == cart_subtotal.text:
#             print("price is same ")
#             print("price text", price_value)
#             print("dummy_ticket:", dummy_ticket.text)
#             print("return_ticket:", return_ticket.text)
#             print("cart_subtotal", cart_subtotal.text)
#         else:
#             print("Price is different")
#             print("price text", price_value)
#             print("dummy_ticket:", dummy_ticket.text)
#             print("return_ticket:", return_ticket.text)
#             print("cart_subtotal", cart_subtotal.text)
#     break
# price_list = driver.find_elements(By.XPATH, "//*[@id='checkout-products']/li/span[2]/span")
# for price in price_list:
#     print(price.text)
price_list = driver.find_element(By.XPATH, "//*[@id='checkout-products']/li/span[2]/span")
for rd_btn in radio_btns:
    rd_btn.click()
    time.sleep(5)
    price_value = price_list.text
    dummy_ticket = driver.find_element(By.XPATH, "//*[@id='order_review']/div[1]/table/tbody/tr/td[2]/span")
    return_ticket = driver.find_element(By.XPATH, "//*[@id='order_review']/div[1]/table/tbody/tr/td[2]/span")
    cart_subtotal = driver.find_element(By.XPATH, "//*[@id='order_review']/div[1]/table/tfoot/tr[1]/td/span")
    if price_value == dummy_ticket.text and price_value == return_ticket.text and price_value == cart_subtotal.text:
        print("price is same ")
        print("price text", price_value)
        print("dummy_ticket:", dummy_ticket.text)
        print("return_ticket:", return_ticket.text)
        print("cart_subtotal", cart_subtotal.text)
    else:
        print("Price is different")
        print("price text", price_value)
        print("dummy_ticket:", dummy_ticket.text)
        print("return_ticket:", return_ticket.text)
        print("cart_subtotal", cart_subtotal.text)