from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePageElement:
    def __init__(self, selector, page):
        self.selector = selector
        self.page = page

    def get_web_element(self):
        element = WebDriverWait(driver=self.page.driver, timeout=10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, self.selector))
        )

        return element


    def is_visible(self):
        web_element = self.get_web_element()

        return web_element.is_displayed()


    

class Page:
    pass
    