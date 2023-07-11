from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# -- Chrome web browser
service_object = Service("C:/Users/aallouche/Documents/Automation/chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service_object)

# -- Firefox web browser
# service_object = Service("C:/Users/aallouche/Documents/Automation/geckodriver-v0.33.0-win-aarch64/geckodriver.exe")
# driver = webdriver.Firefox(service=service_object)

# -- Edge web browser
# service_object = Service("C:/Users/aallouche/Documents/Automation/edgedriver_win64/msedgedriver.exe")
# driver = webdriver.Edge(service=service_object)


# Maximize the window
driver.maximize_window()

# Get the driver to open the url passed
driver.get("https://espn.com")

# Get title of the webpage
title_page = driver.title
print(title_page)

# Get url of the current web page holds by driver
current_url = driver.current_url
print(current_url)

driver.get("https://www.espn.com/nhl/")

# Minimize the window
driver.minimize_window()

# Go back to the previous page
driver.back()

# Refresh the current page
driver.refresh()

# Go forward to the next page
driver.forward()

# Close the web page
driver.close()