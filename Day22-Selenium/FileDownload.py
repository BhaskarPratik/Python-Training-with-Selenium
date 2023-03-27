import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

location = os.getcwd()


def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    ser_obj = Service("E:\Drivers\chromedriver_win32\chromedriver.exe")
    # download the file in desired location
    prefs = {"download.default_directory": location}
    chrome_option = webdriver.ChromeOptions()
    chrome_option.add_experimental_option("detach", True)
    chrome_option.add_experimental_option("prefs", prefs)
    chrome_option.add_argument("--disable-infobars")
    chrome_option.add_argument("start-maximized")
    chrome_option.add_argument("--disable-extensions")

    # Pass the argument 1 to allow and 2 to block
    chrome_option.add_experimental_option(
        "prefs", {"profile.default_content_setting_values.notifications": 1}
    )
    driver = webdriver.Chrome(service=ser_obj, options=chrome_option)
    return driver


# driver = chrome_setup()
# driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
# driver.maximize_window()
#
# btn_download = driver.find_element(By.XPATH, "//*[@id='table-files']/tbody/tr[1]/td[5]/a")
# time.sleep(5)
# btn_download.click()


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
# driver = edge_setup()
# driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
# driver.maximize_window()
# driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()
# time.sleep(10)


def firefox_setup():
    from selenium.webdriver.firefox.service import Service
    from webdriver_manager.firefox import GeckoDriverManager
    # ser_obj = Service("E:\Drivers\geckodriver-v0.32.2-win32\geckodriver.exe")
    firefox_option = webdriver.FirefoxOptions()
    firefox_option.set_preference("browser.download.folderList",
                                  2)  # 0= desktop, 1= default location 2 = desired location
    firefox_option.set_preference("browser.download.manager.showWhenStarting", False)
    firefox_option.set_preference("browser.download.dir", location)
    firefox_option.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/octet-stream")
    driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))

    return driver


driver = firefox_setup()
driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()
driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/a[1]").click()
