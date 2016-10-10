from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()

driver.get("http://www.python.org")

elem = driver.find_element_by_id("id-search-field")
elem.clear()
elem.send_keys('pycon')
elem.send_keys(Keys.Enter)

assert "Not found" not in driver.page_source

driver.close()

