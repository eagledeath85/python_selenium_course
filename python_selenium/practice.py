from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = 'https://rahulshettyacademy.com/AutomationPractice/'

# -- Chrome web browser
options = webdriver.ChromeOptions()

service_object = Service("C:/Users/aallouche/Documents/Automation/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

# Setup wait for later
wait = WebDriverWait(driver, 10)

driver.get(URL)
driver.maximize_window()
options.add_experimental_option("detach", True)

# Tick the radio 1 button and check the checkbox Option 1
driver.find_element(By.XPATH, "//input[@value='radio1']").click()
driver.find_element(By.CSS_SELECTOR, "#checkBoxOption1").click()


# ------------------------------------------------------------------------

# Get the id of the original tab
original_tab = driver.current_window_handle

# Check no tab is already opened
assert len(driver.window_handles) == 1

# Click on "Open Tab" button and assert a new tab is opened
driver.find_element(By.ID, "opentab").click()

# Wait for the new tab to open
wait.until(EC.number_of_windows_to_be(2))

# Loop through until we find a new window handle
for window_handle in driver.window_handles:
    if window_handle != original_tab:
        driver.switch_to.window(window_handle)
        break

wait.until(EC.title_is(driver.title))
assert "QAClick Academy" in driver.title, f"Text is missing"