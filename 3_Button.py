from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

browser = webdriver.Chrome()
action = ActionChains(browser)

try:
    link = 'https://demoqa.com/buttons'
    browser.get(link)

    dynamic_click = browser.find_element(By.CSS_SELECTOR, 'div:nth-child(3)>.btn.btn-primary').click()

    answer = browser.find_element(By.ID, 'dynamicClickMessage')
    text = 'You have done a dynamic clic'
    if text == answer.text:
        print('ok')
    else: print('error dynamic_click')

    double_click = browser.find_element(By.CSS_SELECTOR, 'div:nth-child(1)>.btn.btn-primary')
    action.double_click(double_click).perform()

    right_click = browser.find_element(By.CSS_SELECTOR, 'div:nth-child(2)>.btn.btn-primary')
    action.context_click(right_click).perform()

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

finally:
    time.sleep(5)
    browser.quit()