from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

ser_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ser_obj, options=chrome_option)
driver.implicitly_wait(10)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

src = driver.find_element(By.XPATH, "//div[@id='box6']")
trg = driver.find_element(By.XPATH, "//div[@id='box106']")

act = ActionChains(driver)
act.drag_and_drop(src, trg).perform()  # drag and drop operation

washington = driver.find_element(By.XPATH,"//div[@id='box3']")
united_state = driver.find_element(By.XPATH,"//div[@id='box103']")
act.drag_and_drop(washington,united_state).perform()
