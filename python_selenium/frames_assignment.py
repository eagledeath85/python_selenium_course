import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

service_object = Service("C:/Users/aallouche/Documents/Automation/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)
action = ActionChains(driver)


driver.implicitly_wait(5)
driver.maximize_window()


URL = 'https://rahulshettyacademy.com/AutomationPractice/'
driver.get(URL)


driver.switch_to.frame("courses-iframe")
driver.find_element(By.XPATH, "(//a[@href='consulting'][normalize-space()='Job Support'])[1]").click()

# Fill in name/phone/email
driver.find_element(By.XPATH, "//input[@name='username']").send_keys("john doe")
driver.find_element(By.ID, "mobileno").send_keys("123456789")
driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys("email@email.com")

# Select language
dropdown = Select(driver.find_element(By.ID, 'programming-language'))
dropdown.select_by_index(2)
dropdown.select_by_value("python")

driver.find_element(By.XPATH, "(//div/input[@id='sharing'])[2]").click()
time.sleep(5)
