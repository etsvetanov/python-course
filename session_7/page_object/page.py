from locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait


class BasePageElement(object):

    def set_value(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        driver.find_element_by_name(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")


class SearchTextElement(BasePageElement):
    locator = 'q'


class BasePage:
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class SearchResultsPage(BasePage):

    def is_results_found(self):
        return "No results found." not in self.driver.page_source