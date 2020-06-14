from selenium import webdriver
import time
import os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element_by_name("firstname").send_keys("David")
    browser.find_element_by_name("lastname").send_keys("Sensi")
    browser.find_element_by_name("email").send_keys("dsensi@gmail.com")

    current_dir = os.path.abspath(os.path.dirname(__file__))  
    file_path = os.path.join(current_dir, 'lesson22_step8.txt')           
    file = browser.find_element_by_css_selector("#file")
    file.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()