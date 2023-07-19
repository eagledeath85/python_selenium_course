import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# -- Chrome web browser
service_object = Service("C:/Users/aallouche/Documents/Automation/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

# Adding implicit wait to the script
driver.implicitly_wait(4)

URL = 'https://rahulshettyacademy.com/angularpractice/'
driver.get(URL)

# Find the Shop button using css regex and click on it
driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()

# Retrieving all the elements (phones) of the webpage
phones = driver.find_elements(By.XPATH, "//div[@class='card h-100']")
assert len(phones) > 0, f"ERROR, list of checkboxes is empty."

# Asserting phone_name is Blackberry. If yes, add it to the cart
for phone in phones:
    phone_name = phone.find_element(By.XPATH, "div/h4/a").text
    if phone_name == "Blackberry":
        phone.find_element(By.XPATH, "div/button").click()
        break


# Go to the checkout page
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

# Click on Checkout button
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()

# Writing in the auto-suggest menu
driver.find_element(By.ID, "country").send_keys("ind")

# Adding an explicit wait, and wait until the class suggestions is present in the webpage code
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

# Click on the desired country
driver.find_element(By.LINK_TEXT, "India").click()

# Click on agree with terms and conditions
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

# Click on Purchase button
driver.find_element(By.XPATH, "//input[@type='submit']").click()

# Retrieving final message
final_message = driver.find_element(By.CSS_SELECTOR, "div[class*='alert-success']").text

# Validating message
assert 'Success' in final_message, f"ERROR, purchase is not complete"

# Closing the session
driver.close()