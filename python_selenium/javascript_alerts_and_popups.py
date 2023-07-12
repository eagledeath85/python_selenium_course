from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# -- Chrome web browser
service_object = Service("C:/Users/aallouche/Documents/Automation/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

URL = 'https://rahulshettyacademy.com/AutomationPractice/'
driver.get(URL)
name = "Tony"


# Enter some text in the alert edit box
driver.find_element(By.CSS_SELECTOR, "input[name='enter-name']").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()

# To make Selenium seeing java/javascript pop-ups alerts, we need to switch from browser mode to alert mode
alert = driver.switch_to.alert

# Get the text from the alert
alert_text = alert.text
print(alert_text)

assert name in alert_text, f"{name} is not present in the text"

# Click on the OK button of the alert
alert.accept()

# Click on the Cancel button of the alert
#alert.dismiss()