from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # seconds
driver.get("http://www.python.org")
elem = driver.find_element_by_id("id-search-field")