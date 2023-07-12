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
driver.implicitly_wait(2)

URL = 'https://rahulshettyacademy.com/seleniumPractise/#/'
driver.get(URL)

driver.find_element(By.CSS_SELECTOR, "input[type='search']").send_keys("ber")
time.sleep(2)

# ---------------------------------------------------------------------
# Webelement chaining Concept: use an upper element to find a lower element in it

# Getting all the results from the previous search
articles = driver.find_elements(By.XPATH, "//div[@class='products']/div")
assert len(articles) > 0

# Accessing the element button from tree architecture using call chaining
# button is at //div[@class='product']/div/button XPath, and each article go up to //div[@class='product']/div XPath
# Therefore we just need to call find_element() on each article
for article in articles:
    article.find_element(By.XPATH, "div/button").click()


# Checkout the cart
driver.find_element(By.CSS_SELECTOR, ".cart-icon").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()


promo_code_field = driver.find_element(By.CSS_SELECTOR, '.promoCode')
is_promo_code_displayed = promo_code_field.is_displayed()

assert is_promo_code_displayed

promo_code_field.send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

# Adding an explicit wait, and wait until the class promoInfo is present in the webpage code
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))

print(driver.find_element(By.CLASS_NAME, "promoInfo").text)
