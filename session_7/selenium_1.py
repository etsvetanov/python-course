from selenium import webdriver

driver = webdriver.Firefox()

driver.get("http://www.python.org")

elem = driver.find_element_by_id("id-search-field")

assert "Not found" not in driver.page_source

driver.close()