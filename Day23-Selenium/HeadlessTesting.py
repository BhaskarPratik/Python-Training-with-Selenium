from selenium import webdriver


def chrome_headless():
    from selenium.webdriver.chrome.service import Service
    ser_obj = Service("E:\Drivers\chromedriver_win32\chromedriver.exe")
    opt = webdriver.ChromeOptions()
    opt.headless = True
    driver = webdriver.Chrome(service=ser_obj, options=opt)
    return driver


def edge_headless():
    from selenium.webdriver.edge.service import Service
    ser_obj = Service("E:\Drivers\edgedriver_win64\msedgedriver.exe")
    opt = webdriver.EdgeOptions()
    opt.headless = True
    driver = webdriver.Edge(service=ser_obj, options=opt)
    return driver


def firefox_headless():
    from selenium.webdriver.firefox.service import Service
    from webdriver_manager.firefox import GeckoDriverManager
    opt = webdriver.FirefoxOptions()
    opt.headless = True
    driver = webdriver.Firefox(service=Service(executable_path=GeckoDriverManager().install()))
    return driver


# driver = chrome_headless()
driver = edge_headless()
# driver = firefox_headless()
driver.get("https://demo.nopcommerce.com/")
print(driver.title)
print(driver.current_url)
driver.quit()
