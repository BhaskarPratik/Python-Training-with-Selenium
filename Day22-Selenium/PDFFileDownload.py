import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

location = os.getcwd()


# def chrome_setup():
#     from selenium.webdriver.chrome.service import Service
#     pref = {"download.default_directory": location,"plugins.always_open_pdf_externally":True}
#     service_obj = Service("E:\Drivers\chromedriver_win32\chromedriver.exe")
#     opt = webdriver.ChromeOptions()
#     opt.add_experimental_option("detach", True)
#     opt.add_experimental_option("prefs", pref)
#     driver = webdriver.Chrome(service=service_obj, options=opt)
#     return driver

# def edge_setup():
#     from selenium.webdriver.edge.service import Service
#     ser_obj = Service("E:\Drivers\edgedriver_win64\msedgedriver.exe")
#     # download the file in desired location
#     prefs = {"download.default_directory": location}
#     edge_option = webdriver.EdgeOptions()
#     edge_option.se
#     edge_option.add_experimental_option("detach",True)
#     edge_option.add_experimental_option("prefs",prefs)
#     driver = webdriver.Edge(service=ser_obj,options=edge_option)
#     return driver

def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    ser_obj = Service("E:\Drivers\geckodriver-v0.32.2-win32\geckodriver.exe")
    firefox_option = webdriver.FirefoxOptions()
    firefox_option.set_preference("browser.download.folderList", 2)  # 0= desktop, 1= default location 2 = desired
    location
    firefox_option.set_preference("browser.download.manager.showWhenStarting", False)
    firefox_option.set_preference("browser.download.dir", location)
    firefox_option.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
    firefox_option.set_preference("pdfjs.disabled", True)  # for pdf
    driver = webdriver.Firefox(service=ser_obj, options=firefox_option)

    return driver


# driver = chrome_setup()
# driver = edge_setup()
driver = firefox_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-pdf-download/")
driver.maximize_window()
time.sleep(10)
driver.find_element(By.XPATH, "//*[@id='table-files']/tbody/tr[1]/td[5]/a").click()
