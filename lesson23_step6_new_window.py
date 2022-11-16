from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)
	browser.find_element(By.CSS_SELECTOR, "button.btn").click()

	new_window = browser.window_handles[1]
	browser.switch_to.window(new_window)

	x = browser.find_element(By.ID, "input_value").text
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))

	browser.find_element(By.ID, "answer").send_keys(calc(x))
	browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
	time.sleep(5)
	browser.quit()