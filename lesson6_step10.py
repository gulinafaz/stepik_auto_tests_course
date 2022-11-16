from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/registration1.html")

    browser.find_element(By.XPATH, "//input[contains(@placeholder, 'first name')]").send_keys("Ivan")
    browser.find_element(By.XPATH, "//input[contains(@placeholder, 'last name')]").send_keys("Petrov")
    browser.find_element(By.XPATH, "//input[contains(@placeholder, 'email')]").send_keys("test@test.com")
    
    browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]").click()

    time.sleep(2)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    browser.quit()


