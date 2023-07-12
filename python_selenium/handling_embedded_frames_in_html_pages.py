
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

URL = "https://the-internet.herokuapp.com/iframe"
driver.get(URL)


# --------------------------------------------------------------------
# It may happen that frames are embedded in a webpage.
# To know that, 2 solutions:
#   1. Ask the developper if there are embedded frames in the tested page
#   2. Inspect the page and look for iframes

# Switch to the frame, then clear the text box and write some text
driver.switch_to.frame('mce_0_ifr')
driver.find_element(By.ID, "tinymce").clear()
driver.find_element(By.ID, "tinymce").send_keys("Sample Text")

# Switch back to the initial scope
driver.switch_to.default_content()

text = driver.find_element(By.CSS_SELECTOR, "h3").text
assert text == "An iFrame containing the TinyMCE WYSIWYG Editor"