#Task 5: website navigation and link check

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Edge()
driver.get("https://www.w3schools.com/html/")
assert "HTML Tutorial" in driver.title
accept_button = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'accept-choices')))
accept_button.click()
try:
    first_menu_element = driver.find_element(By.LINK_TEXT, "HTML Elements")
    first_menu_element.click()
    first_menu_page_appear = WebDriverWait(driver, 10).until(expected_conditions.title_contains("HTML Elements"))
    assert "HTML Elements" in driver.title, "'HTML Elements text is not visible in page title"
    driver.back()
    assert "HTML Tutorial" in driver.title
    sec_menu_element = driver.find_element(By.LINK_TEXT, "HTML Styles")
    sec_menu_element.click()
    sec_menu_page_appear = WebDriverWait(driver, 10).until(expected_conditions.title_contains("HTML Styles"))
    assert "HTML Styles" in driver.title, "'HTML Styles text is not visible in page title"
    driver.back()
    assert "HTML Tutorial" in driver.title
    third_menu_element = driver.find_element(By.LINK_TEXT, "HTML Images")
    third_menu_element.click()
    third_menu_page_appear = WebDriverWait(driver, 10).until(expected_conditions.title_contains("HTML Images"))
    assert "HTML Images" in driver.title, "'HTML Images text is not visible in page title"

finally:
    driver.close()
