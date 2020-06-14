from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

	link = "http://suninjuly.github.io/explicit_wait2.html"
	browser=webdriver.Chrome()
	browser.get(link)

	button = WebDriverWait(browser, 12).until(
	EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    	)
	button.click()
	message = browser.find_element_by_id("verify_message")

assert "successful" in message.text