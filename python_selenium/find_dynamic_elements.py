import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# -- Chrome web browser
service_object = Service("C:/Users/aallouche/Documents/Automation/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

URL = 'https://rahulshettyacademy.com/dropdownsPractise/'
driver.get(URL)

# -----------------------------------------------------------
# Auto-Suggested dropdown menus
# 1. Find the field where to write and start writing
driver.find_element(By.ID, "autosuggest").send_keys("ind")
# 2. Add a timer to give time to the auto-suggested menu to display all the matching options
time.sleep(2)
# 3. Retrieve all the elements from the suggested list with CSS Selector locator with find_elements() method
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a") # list of WebElements
assert len(countries) != 0, f"ERROR, list of countries is empty"

for country in countries:
    if country.text == "India":
        country.click()
        break

time.sleep(2)
# text works only on values that are already present in the webpage on first loading
# When retrieving a text value from an auto-suggested menu, we use the get_attribute("value") method
# Get the text value of the selected country
print(driver.find_element(By.ID, "autosuggest").get_attribute("value")) # will print India

expected_value = "India"
assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == expected_value, f"Error: {expected_value} is missing"