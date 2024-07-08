from selenium.webdriver.common.by import By
from logic.base_page_app import BasePageApp


class MainPage(BasePageApp):
    LOGIN_TITLE = '//h1[@class="post-title"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._login_title = self._driver.find_element(By.XPATH, self.LOGIN_TITLE)

    def login_title_is_displayed(self):
        return self._login_title.is_displayed()

    def get_login_title_text(self):
        return self._login_title.text
