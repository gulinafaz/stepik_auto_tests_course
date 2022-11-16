from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "https://suninjuly.github.io/selects1.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	x = browser.find_element(By.ID, "num1").text
	y = browser.find_element(By.ID, "num2").text
	s = str(int(x) + int(y))
	Select(browser.find_element(By.ID, "dropdown")).select_by_value(s)
	browser.find_element(By.CSS_SELECTOR, "button.btn").click()
	 
	
finally:
	time.sleep(5)
	browser.quit()
