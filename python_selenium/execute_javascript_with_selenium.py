import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# Setting the webbrowser on background when running the tests
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")


# -- Chrome web browser
service_object = Service("C:/Users/aallouche/Documents/Automation/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_object, options=chrome_options)

# Adding implicit wait to the script
driver.implicitly_wait(5)
driver.maximize_window()

URL = 'https://rahulshettyacademy.com/AutomationPractice/'
driver.get(URL)

# Execute javascript to scroll down to the end of the webpage
driver.execute_script("window.scroll(0, document.body.scrollHeight);")

# Take screenshot of the current view in the webpage and save it as jpg file
driver.get_screenshot_as_file("screenshot.png")