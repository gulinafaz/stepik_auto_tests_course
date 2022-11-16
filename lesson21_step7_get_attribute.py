from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

try:
	browser = webdriver.Chrome()
	browser.get(link)

	x = browser.find_element(By.ID, "treasure").get_attribute("valuex")
	def calc(x):
		return str(math.log(abs(12*math.sin(int(x)))))
	y = calc(x)

	browser.find_element(By.ID, "answer").send_keys(y)
	browser.find_element(By.ID, "robotCheckbox").click()
	browser.find_element(By.ID, "robotsRule").click()
	browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
	browser.quit()
