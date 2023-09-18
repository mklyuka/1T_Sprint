from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
action = ActionChains(browser)

try:
    link = 'https://demoqa.com/slider'
    browser.get(link)
    browser.implicitly_wait(10)

    slider = browser.find_element(By.CSS_SELECTOR, '.range-slider.range-slider--primary')

    action.click_and_hold(slider).move_by_offset(1, 0).release().perform()

    slider_value = browser.find_element(By.ID, 'sliderValue')
    check_value = slider_value.get_attribute('value')

    if check_value == '50':
        print('ok check_value')
    else:
        print('error check_value')

finally:
    time.sleep(5)
    browser.quit()