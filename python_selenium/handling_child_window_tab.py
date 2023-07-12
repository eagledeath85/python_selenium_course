import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# -- Chrome web browser
service_object = Service("C:/Users/aallouche/Documents/Automation/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

# Adding implicit wait to the script
driver.implicitly_wait(5)
driver.maximize_window()

URL = 'https://the-internet.herokuapp.com/windows'
driver.get(URL)


# Selenium uses scopes to determine the active webpage/tab.
# To navigate to another page/tab, we need to move to the desired page/tab first
# We use the switch_to.window() method, and we pass to it the name of the window we want to switch to
driver.find_element(By.LINK_TEXT, "Click Here").click()

# window_handles property will return the name of all windows in a list
windows_name = driver.window_handles

# By default the index 0 is the first window opened by Selenium
driver.switch_to.window(windows_name[1])

assert driver.find_element(By.CSS_SELECTOR, "h3").text == "New Window", f"Text doesn't match"
driver.close()
