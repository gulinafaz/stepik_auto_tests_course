from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
	y = calc(x)

	browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
	browser.find_element(By.CSS_SELECTOR, "[type='checkbox']").click()
	browser.find_element(By.CSS_SELECTOR, "[value='robots']").click()
	browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
	browser.quit()
