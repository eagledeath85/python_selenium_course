import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# -- Chrome web browser
service_object = Service("C:/Users/aallouche/Documents/Automation/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

# Adding implicit wait to the script
driver.implicitly_wait(5)
driver.maximize_window()

URL = 'https://rahulshettyacademy.com/seleniumPractise/#/offers'
driver.get(URL)


# ----------------------------------------------------------
# We can sort tables using Selenium. For example, tables that have fields that can be sorted, like databases
# Steps in order to achieve sorting
# 1. Click on column header to sort the items
# 2. Collect items name for this specific column -> items_list
# 3. Sort this list with sort() method -> items_list_sorted
# 4. Assert items_list == items_list_sorted

# 1. Click on column header to sort the items
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

# 2. Collect items name for this specific column -> items_list
items_name_list = []
items_list = driver.find_elements(By.XPATH, "//tr/td[1]")
for item in items_list:
    items_name_list.append(item.text)

# Make a deep copy of the original list
original_browser_sorted_list = items_name_list.copy()

# 3. Sort this list with sort() method -> items_list_sorted
# This will also affect the items_list list, that's why we previously made a copy
items_name_list.sort()

# 4. Assert items_list == items_list_sorted
assert items_name_list == original_browser_sorted_list