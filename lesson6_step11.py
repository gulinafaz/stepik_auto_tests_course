from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.XPATH, "//div[@class='first_block']//input[contains(@class, 'first')]").send_keys("Ivan")
    # browser.find_element(By.XPATH, "//div[@class='first_block']//input[contains(@class, 'second')]").send_keys("Petrov")
    browser.find_element(By.XPATH, "//div[@class='first_block']//input[contains(@class, 'third')]").send_keys("test@test.com")
    
    browser.find_element(By.XPATH, "//button[contains(text(), 'Submit')]").click()

    time.sleep(2)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    browser.quit()


