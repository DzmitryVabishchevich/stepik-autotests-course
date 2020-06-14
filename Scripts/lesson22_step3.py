from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x1,x2):
  return str(int(x1)+int(x2))

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x1 = browser.find_element_by_css_selector("#num1").text
    x2 = browser.find_element_by_css_selector("#num2").text
    x_answer = calc(x1,x2)

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(x_answer)

    button = browser.find_element_by_css_selector("button.btn.btn-default")
    button.click()

finally:
    time.sleep(10)
    browser.quit()