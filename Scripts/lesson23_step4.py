from selenium import webdriver
import time
import math

def function(x):
	return str(math.log((abs(12*math.sin(int(x))))))

try:
     link = "http://suninjuly.github.io/alert_accept.html"
     browser=webdriver.Chrome()
     browser.get(link)

     browser.find_element_by_css_selector("button.btn").click()
     alert = browser.switch_to.alert
     alert.accept()

     x = browser.find_element_by_css_selector("#input_value").text
     y = function(x)
     browser.find_element_by_css_selector("#answer").send_keys(y)
     browser.find_element_by_css_selector("button.btn-primary").click()

finally:
     time.sleep(10)
     browser.quit()