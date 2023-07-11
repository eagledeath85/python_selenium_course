from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# -- Chrome web browser
service_object = Service("C:/Users/aallouche/Documents/Automation/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

URL = 'https://rahulshettyacademy.com/angularpractice/'

driver.get(URL)

# Find the email field using NAME locator, and write in the field using send_keys()
driver.find_element(By.NAME, "email").send_keys("test_email@email.com")

# Find the password field using ID locator, and write in the field using send_keys()
driver.find_element(By.ID, "exampleInputPassword1").send_keys("123456789")

# Click on the checkbox
driver.find_element(By.ID, "exampleCheck1").click()

# Fill the name field using CSS Selector and standard css syntax
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("namenamename")

# Click on Studnet radio button using CSS Selector and id syntax
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()

# Find the Submit button by XPath locator. to submit the form
# XPath is built following the syntax: tagname[@attribute='value']
#Thos values are determined by looking in the Inspector tool
# Here tagname=input, attribut=type, value=submit
driver.find_element(By.XPATH, "//input[@type='submit']").click()

# Once the form is submitted, we want to check whether it's successfully submitted
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert message != "The Form has been submitted successfully!.", f"ERROR, message is incorrect"

driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("hello there")

# Clear the field
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()

driver.implicitly_wait(60)