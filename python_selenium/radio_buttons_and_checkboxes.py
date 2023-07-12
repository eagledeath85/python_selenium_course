from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# -- Chrome web browser
service_object = Service("C:/Users/aallouche/Documents/Automation/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

URL = 'https://rahulshettyacademy.com/AutomationPractice/'
driver.get(URL)

# -------------------------------------------------
# Let's assume that ID, name and value are missing when spying with the Inspector
# Get all the checkboxes from the webpages by get_attribute()
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
assert len(checkboxes) > 0, f"ERROR, list of checkboxes is empty."

for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break


# -------------------------------------------------
# If we know the radio buttons won't change then we can handle it like this

radio_buttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")       # .radioButton == input[class='radioButton']
radio_button_3 = radio_buttons[2]
radio_button_3.click()
assert radio_button_3.is_selected()


# -------------------------------------------------
# Check whether a field is displayed
driver.find_element(By.ID, "displayed-text").is_displayed()
assert driver.find_element(By.ID, "displayed-text").is_displayed()

driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()