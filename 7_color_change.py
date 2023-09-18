from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

browser = webdriver.Chrome()

try:
    link = 'https://demoqa.com/dynamic-properties'
    browser.get(link)

    current_color = browser.find_element(By.ID, 'colorChange').value_of_css_property('color')
    expected_color = 'rgba(220, 53, 69, 1)'

    while current_color != expected_color:
        time.sleep(1)
        current_color = browser.find_element(By.ID, 'colorChange').value_of_css_property('color')
    else:
        color_change = browser.find_element(By.ID, 'colorChange').click()


finally:
    time.sleep(5)
    browser.quit()