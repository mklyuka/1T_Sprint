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
    email.send_keys('aspush@inbox.ru')

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

    # Проверка отображения введенных данных
    check_name = browser.find_element(By.CSS_SELECTOR, '.mb-1:nth-child(1)')
    text_name = check_name.text

    if text_name == 'Name: Александр Сергеевич Пушкин':
        print('ok check_name')
    else:
        print('error check_name')

    check_email = browser.find_element(By.CSS_SELECTOR, '.mb-1:nth-child(2)')
    text_email = check_email.text

    if text_email == 'Email: aspush@inbox.ru':
        print('ok check_email')
    else:
        print('error check_email')

    check_currentAddress = browser.find_element(By.CSS_SELECTOR, '.mb-1:nth-child(3)')
    text_currentAddress = check_currentAddress.text

    if (text_currentAddress ==
            'Current Address: Пушкинская ул., 1, пгт Пушкинские Горы, Пушкиногорский р-н, Псковская область, 181370'):
        print('ok check_currentAddress')
    else:
        print('error check_currentAddress')

    check_permanentAddress = browser.find_element(By.CSS_SELECTOR, '.mb-1:nth-child(4)')
    text_permanentAddress = check_permanentAddress.text

    if text_permanentAddress == 'Permanent Address: с. Михайловское, Псковская обл., Россия, 181370':
        print('ok check_permanentAddress')
    else:
        print('error check_permanentAddress')


finally:
    browser.quit()