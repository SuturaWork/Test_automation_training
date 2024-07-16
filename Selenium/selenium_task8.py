#Task 8: handling popup window

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


driver = webdriver.Edge()
driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")
assert "W3Schools Tryit Editor" in driver.title
accept_button = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'accept-choices')))
accept_button.click()
try:
    driver.switch_to.frame("iframeResult")
    try_button = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Try it']")))
    try_button.click()
    WebDriverWait(driver, 10).until(expected_conditions.alert_is_present())
    popup = driver.switch_to.alert
    popup.accept()
    try:
        WebDriverWait(driver, 5).until(expected_conditions.alert_is_present())
        print("Popup is still visible.")
    except:
        print("Popup is closed.")

finally:
    driver.close()
