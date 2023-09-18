from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

browser = webdriver.Chrome()

try:
    link = 'https://demoqa.com/dynamic-properties'
    browser.get(link)

    enable_after = WebDriverWait(browser, 10).until(
        expected_conditions.element_to_be_clickable((By.ID, 'enableAfter'))
    )
    enable_after.click()

finally:
    time.sleep(5)
    browser.quit()