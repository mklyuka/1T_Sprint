from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

try:
    link = 'https://demoqa.com/dynamic-properties'
    browser.get(link)

    browser.implicitly_wait(10)
    visible_after = browser.find_element(By.ID, 'visibleAfter').click()

finally:
    time.sleep(5)
    browser.quit()