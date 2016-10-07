from selenium import webdriver
from unittest import TestCase
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class HomePageTest(TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_field(self):
        self.driver.get("http://www.python.org")
        elem = self.driver.find_element_by_id("id-search-field")
        elem.clear()
        elem.send_keys('pycon')
        elem.send_keys(Keys.RETURN)

        self.assertNotIn('No results found', self.driver.page_source)

    def test_documentation_button(self):
        self.driver.get("http://www.python.org")

        elem = self.driver.find_element_by_link_text('Documentation')
        link_path = elem.get_attribute('href')
        self.assertTrue(link_path.endswith('/doc/'))

    def test_documentation_button_opens_doc_page(self):
        self.driver.get("http://www.python.org")

        elem = self.driver.find_element_by_css_selector("#documentation a")
        elem.click()


        self.assertEqual('Our Documentation | Python.org', self.driver.title)

    def test_about_menu(self):
        self.driver.get("http://www.python.org")
        about_button = self.driver.find_element_by_css_selector('#about')
        action_chain = ActionChains(self.driver).move_to_element(about_button)
        action_chain.perform()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#about .tier-2.element-1')))

        sub_menu = self.driver.find_element_by_css_selector('#about li.tier-2.element-1')

        self.assertTrue(sub_menu.location['y'] > 0)


    def tearDown(self):
        self.driver.close()


