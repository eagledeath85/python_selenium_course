import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# -- Chrome web browser
service_object = Service("C:/Users/aallouche/Documents/Automation/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

# Adding implicit wait to the script
driver.implicitly_wait(5)
driver.maximize_window()

URL = 'https://rahulshettyacademy.com/AutomationPractice/'
driver.get(URL)

# ActionChains() allows to perform advanced actions like hover above a button, right-click, scroll up/down, double-click, drag/drop, ...
# Create an action object by calling ActionChains class and passing the driver to it
action = ActionChains(driver)

# Hover above an element using move_to_element() method and passing to it the element we want to hover
# MUST finish whatever the action is with perform() method to complete the action
action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()

# Right-click on an element using context_click() method and passing to it the element we want to right-click
#   action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
time.sleep(5)
