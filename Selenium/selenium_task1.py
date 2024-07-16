#Task 1: Google Search

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Edge()
driver.get("https://www.google.com")
try:
    accept_button = driver.find_element(By.ID, 'L2AGLb')
    accept_button.click()
    assert "Google" in driver.title
    search_field = driver.find_element(By.NAME, 'q')
    search_field.clear()
    search_field.send_keys("Selenium Python")
    search_field.send_keys(Keys.RETURN)
    result_appear = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'h3')))
    first_result = driver.find_element(By.CSS_SELECTOR, 'h3')
    assert "Selenium" in first_result.text, "'Selenium is not contained in first result"
finally:
    driver.close()
