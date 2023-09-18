from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

try:
    link = 'https://demoqa.com/text-box'
    browser.get(link)

    # переменная = поле ввода Username
    fullname = browser.find_element(By.CSS_SELECTOR, 'form>.mt-2.row>.col-md-9.col-sm-12>input[placeholder="Full Name"]')
    # Вводим данные в поле ввода
    fullname.send_keys('Александр Сергеевич Пушкин')

    email = browser.find_element(By.CSS_SELECTOR, 'form>.mt-2.row>.col-md-9.col-sm-12>input[placeholder="name@example.com"]')
    email.send_keys('aspush@inbox.ru')

    current_address = browser.find_element(By.CSS_SELECTOR, 'form>.mt-2.row>.col-md-9.col-sm-12>textarea[placeholder="Current Address"]')
    current_address.send_keys('Пушкинская ул., 1, пгт Пушкинские Горы, Пушкиногорский р-н, Псковская область, 181370')

    permanent_address = browser.find_element(By.CSS_SELECTOR, 'form>.mt-2.row:nth-child(4)>.col-md-9.col-sm-12>.form-control')
    permanent_address.send_keys('с. Михайловское, Псковская обл., Россия, 181370')

    # прокрутка страницы
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # переменная = кнопка Login
    button = browser.find_element(By.CSS_SELECTOR, 'form>.mt-2.justify-content-end.row>.text-right.col-md-2.col-sm-12>.btn')
    # клик по кнопке Login
    button.click()

finally:
    time.sleep(5)
    browser.quit() # закрыть браузер