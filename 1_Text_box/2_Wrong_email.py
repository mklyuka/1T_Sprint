from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)

try:
    link = 'https://demoqa.com/text-box'
    browser.get(link)

    # Заполнение формы
    browser.implicitly_wait(3)
    fullname = browser.find_element(By.CSS_SELECTOR,
                                    'form>.mt-2.row>.col-md-9.col-sm-12>input[placeholder="Full Name"]')
    fullname.send_keys('Александр Сергеевич Пушкин')

    email = browser.find_element(By.CSS_SELECTOR,
                                 'form>.mt-2.row>.col-md-9.col-sm-12>input[placeholder="name@example.com"]')
    email.send_keys('aspush@inboxru')

    current_address = browser.find_element(By.CSS_SELECTOR,
                                           'form>.mt-2.row>.col-md-9.col-sm-12>textarea[placeholder="Current Address"]')
    current_address.send_keys('Пушкинская ул., 1, пгт Пушкинские Горы, Пушкиногорский р-н, Псковская область, 181370')

    permanent_address = browser.find_element(By.CSS_SELECTOR,
                                             'form>.mt-2.row:nth-child(4)>.col-md-9.col-sm-12>.form-control')
    permanent_address.send_keys('с. Михайловское, Псковская обл., Россия, 181370')

    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    button = browser.find_element(By.CSS_SELECTOR,
                                  'form>.mt-2.justify-content-end.row>.text-right.col-md-2.col-sm-12>.btn')
    button.click()

    # проверка ошибки поля email
    wrong_email = email.get_attribute('class')
    if 'field-error' in wrong_email:
        print('ok wrong_email')
    else:
        print('error wrong_email')

finally:
    browser.quit()