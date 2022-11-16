from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = " http://suninjuly.github.io/find_xpath_form "

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.NAME, "first_name").send_keys("Ivan")
    browser.find_element(By.NAME, "last_name").send_keys("Petrov")
    browser.find_element(By.CLASS_NAME, "city").send_keys("Smolensk")
    browser.find_element(By.ID, "country").send_keys("Russia")
    browser.find_element(By.XPATH, '//button[contains(text(), "Submit")]').click()

finally:
    time.sleep(5)
    browser.quit()


