from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# -- Chrome web browser
service_object = Service("C:/Users/aallouche/Documents/Automation/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

URL = 'https://rahulshettyacademy.com/client'

driver.get(URL)
driver.maximize_window()
# Look for the text "Forgot password?" link on the web page and click on it
driver.find_element(By.LINK_TEXT, "Forgot password?").click()

# Find the email field where we want to put the email address
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("user@user.com")

# We can also use the following syntax, using the tree architecture to find our element: "//form/div[2]/input"
# Here we access to the password field and write it
driver.find_element(By.XPATH, "//form/div[2]/input").send_keys("123456789")

# Using CSS Selector and tree architecture, it will look like this
# driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("12345678")

# Other way, the simplest using CSS Selector
driver.find_element(By.CSS_SELECTOR, '#confirmPassword').send_keys("123456789")

# Finally click on the "Save Password" button
driver.find_element(By.XPATH, "//button[@type='submit']").click()

# Or by using the text in the button:
# driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()
