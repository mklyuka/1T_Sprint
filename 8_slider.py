from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

browser = webdriver.Chrome()
action = ActionChains(browser)

try:
    link = 'https://demoqa.com/slider'
    browser.get(link)

    slider = browser.find_element(By.CSS_SELECTOR, '.range-slider.range-slider--primary')

    action.click_and_hold(slider).move_by_offset(1, 0).release().perform()

finally:
    time.sleep(5)
    browser.quit()