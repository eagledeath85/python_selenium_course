
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# -- Chrome web browser
service_object = Service("C:/Users/aallouche/Documents/Automation/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

# Adding implicit wait to the script
driver.implicitly_wait(5)
driver.maximize_window()

URL = "https://rahulshettyacademy.com/loginpagePractise/"
driver.get(URL)

# Click on blinking text and open a new tab
driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()

# Retrieve all the tab names
windows_names = driver.window_handles

# Switching to the last one opened
driver.switch_to.window(windows_names[-1])

# Retrieving email value
email = driver.find_element(By.CSS_SELECTOR, "div p a").text

# Switch back to the first tab
driver.switch_to.window(windows_names[0])

# Writing credentials into the relevant fields
driver.find_element(By.XPATH, "//input[@name='username']").send_keys(email)
driver.find_element(By.XPATH, "//input[@name='password']").send_keys("123456789")
driver.find_element(By.CSS_SELECTOR, "input[type='checkbox']").click()
driver.find_element(By.ID, "signInBtn").click()

# Retrieve the Incorrect word
wait = WebDriverWait(driver, 10)
message = driver.find_element(By.XPATH, "//form[@id='login-form']//strong/..")
wait.until(expected_conditions.visibility_of(message))
print(message.text)