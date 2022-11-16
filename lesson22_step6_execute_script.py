from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import math

link = "http://suninjuly.github.io/execute_script.html"

try:
 	browser = webdriver.Chrome()
 	browser.get(link)
 	x = browser.find_element(By.ID, "input_value").text

 	def calc(x):
 		return str(math.log(abs(12*math.sin(int(x)))))

 	browser.find_element(By.ID, "answer").send_keys(calc(x))
 	checkbox = browser.find_element(By.ID, "robotCheckbox")
 	browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
 	checkbox.click()
 	browser.find_element(By.ID, "robotsRule").click()
 	browser.find_element(By.CSS_SELECTOR, "button.btn").click()




finally:
 	time.sleep(5)
 	browser.quit()
