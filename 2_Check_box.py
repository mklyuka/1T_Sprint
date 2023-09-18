from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()

try:
    link = 'https://demoqa.com/checkbox'
    browser.get(link)

    drop_home = browser.find_element(By.CSS_SELECTOR, '')
    drop_home.click()

    drop_desktop = browser.find_element(By.CSS_SELECTOR, '')
    drop_desktop.click()

    drop_documents = browser.find_element(By.CSS_SELECTOR, '')
    drop_documents.click()

    drop_downloads = browser.find_element(By.CSS_SELECTOR, '')
    drop_downloads.click()

    drop_workspace = browser.find_element(By.CSS_SELECTOR, '')
    drop_workspace.click()

    drop_office = browser.find_element(By.CSS_SELECTOR, '')
    drop_office.click()

    check_excel = browser.find_element(By.CSS_SELECTOR, '')
    check_excel.click()

    check_general = browser.find_element(By.CSS_SELECTOR, '')
    check_general.click()

    check_veu = browser.find_element(By.CSS_SELECTOR, '')
    check_veu.click()

    check_commands = browser.find_element(By.CSS_SELECTOR, '')
    check_commands.click()

finally:
    time.sleep(5)
    browser.quit()