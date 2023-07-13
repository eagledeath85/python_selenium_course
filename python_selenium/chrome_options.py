from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# Chrome Options examples
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

# -- Chrome web browser
service_object = Service("C:/Users/aallouche/Documents/Automation/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_object, options=chrome_options)

URL = 'https://rahulshettyacademy.com/angularpractice/'
driver.get(URL)

print(driver.title)