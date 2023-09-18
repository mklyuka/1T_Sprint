from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

try:
    link = 'https://demoqa.com/alerts'
    browser.get(link)

    time_alert = browser.find_element(By.ID, 'timerAlertButton').click()
    time.sleep(6)
    alert = browser.switch_to.alert
    alert.accept()

    confirm_alert = browser.find_element(By.ID, 'confirmButton').click()
    time.sleep(3)
    alert.dismiss()

    browser.execute_script("window.scrollBy(0, 100);")

    prompt_alert = browser.find_element(By.ID, 'promtButton').click()
    time.sleep(3)
    text_prompt = 'Please enter your name'
    text_alert = alert.text
    if text_prompt == text_alert:
        print('ok prompt_text')
    else: print('error prompt_text')
    alert.send_keys('Maxim')
    time.sleep(3)
    alert.accept()


finally:
    time.sleep(5)
    browser.quit()