#Task 2: Find hidden button and click

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

driver = webdriver.Edge()
driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
try:
    accept_button = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'accept-choices')))
    accept_button.click()
    assert "How To Toggle Between Hiding And Showing an Element" in driver.title
    toggle_button = driver.find_element(By.XPATH, "//button[text()='Toggle Hide and Show']")
    toggle_button.click()
    time.sleep(1)
    hidden_message = driver.find_element(By.ID, "myDIV")
    assert hidden_message.is_displayed(), "Hidden message is not displayed"
finally:
    driver.close()
