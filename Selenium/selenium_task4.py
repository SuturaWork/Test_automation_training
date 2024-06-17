#Task 4: reload a dinamic page

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


driver = webdriver.Edge()
driver.get("https://the-internet.herokuapp.com/dynamic_content?with_content=static")
try:
    page_appear = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'h3')))
    first_content = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]')
    first_content_text = first_content.text
    print(f"Initial content: {first_content_text}")
    driver.refresh()
    page_appear_again = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, 'h3')))
    reloaded_content = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]')
    reloaded_content_text = reloaded_content.text
    print(f"Reloaded content: {reloaded_content_text}")
    assert first_content_text != reloaded_content_text, "Content did not change after reloading"
finally:
    driver.close()
