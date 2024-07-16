#Task 3: fill a form

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Edge()
driver.get("https://www.w3schools.com/html/html_forms.asp")
try:
    accept_button = driver.find_element(By.ID, 'accept-choices')
    accept_button.click()
    assert "HTML Forms" in driver.title
    first_name = driver.find_element(By.ID, "fname")
    first_name.clear()
    first_name.send_keys("Dora")
    last_name = driver.find_element(By.ID, "lname")
    last_name.clear()
    last_name.send_keys("Szeli")
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Submit']")
    submit_button.click()
    WebDriverWait(driver, 10).until(expected_conditions.number_of_windows_to_be(2))
    driver.switch_to.window(driver.window_handles[1])
    success_message = driver.find_element(By.XPATH, "//*[contains(text(), 'The server has processed your input and returned this answer.')]")
    assert success_message.is_displayed(), "Success message did not appear"
finally:
    driver.close()
