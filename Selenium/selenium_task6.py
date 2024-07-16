#Task 6: image upload

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


driver = webdriver.Edge()
driver.get("https://www.w3schools.com/howto/howto_html_file_upload_button.asp")
assert "File Upload Button" in driver.title
accept_button = WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'accept-choices')))
accept_button.click()
try:
    upload_button = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.ID, 'myFile')))
    wait = WebDriverWait(driver, 5)
    file_path = 'C:/Users/dszeleczkei/Test_automation_training/Selenium/image_for_upload.png'
    upload_button.send_keys(file_path)
    success_upload = upload_button.get_attribute('value')
    image_check = file_path.split('/')[-1]
    assert image_check in success_upload, "Image is not uploaded."
    print(f"File upload was successful: {image_check}")

finally:
    driver.close()
