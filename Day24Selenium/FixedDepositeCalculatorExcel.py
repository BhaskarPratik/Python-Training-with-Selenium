import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Day24Selenium import ExcelUtils

ser_obj = Service("E:\Drivers\chromedriver_win32\chromedriver.exe")
opt = Options()
opt.add_experimental_option("detach", True)
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument("--disable-notification")

# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option(
    "prefs", {"profile.default_content_setting_values.notifications": 1}
)
driver = webdriver.Chrome(service=ser_obj, options=opt)
driver.implicitly_wait(10)
driver.get(
    "https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001"
    ".html?classic=true")
driver.maximize_window()
file = "C:/Users/Mangesh/OneDrive/Desktop/caldata.xlsx"
rows = ExcelUtils.getRowCount(file,"Sheet 1")

# reading data from excel

for r in range(2, rows + 1):
    princ = ExcelUtils.readData(file, "Sheet 1", r, 1)
    ROI = ExcelUtils.readData(file, "Sheet 1", r, 2)
    period1 = ExcelUtils.readData(file, "Sheet 1", r, 3)
    period2 = ExcelUtils.readData(file, "Sheet 1", r, 4)
    freq = ExcelUtils.readData(file, "Sheet 1", r, 5)
    exp_mtValue = ExcelUtils.readData(file, "Sheet 1", r, 6)

    # passing data to the application
    driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(princ)
    driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(ROI)
    driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(period1)
    period_drp = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
    period_drp.select_by_visible_text(period2)
    freq_drp = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
    freq_drp.select_by_visible_text(freq)
    driver.find_element(By.XPATH, "//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']").click()
    act_mt_value = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text

    # validation
    if float(exp_mtValue) == float(act_mt_value):
        print("Test Passed")
        ExcelUtils.writeData(file,"Sheet 1",r,8,"Passed")
        ExcelUtils.fillGreenColor(file,"Sheet 1",r,8)
    else:
        print("Test Failed")
        ExcelUtils.writeData(file,"Sheet 1",r,8,"Failed")
        ExcelUtils.fillRedColor(file,"Sheet 1",r,8)
    driver.find_element(By.XPATH,"//img[@src = 'https://images.moneycontrol.com/images/mf_revamp/btn_clear.gif']").click()
    time.sleep(2)
driver.quit()