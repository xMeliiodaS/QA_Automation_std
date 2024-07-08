from selenium.webdriver.common.by import By
from logic.base_page_app import BasePageApp
from selenium import common as c


class LoginPage(BasePageApp):
    USER_NAME_INPUT = '//input[@id="username"]'
    PASSWORD_INPUT = '//input[@id="password"]'
    SUBMIT_BUTTON = '//button[@id="submit"]'

    def __init__(self, driver):
        super().__init__(driver)
        try:
            self._user_name_input = self._driver.find_element(By.XPATH, self.USER_NAME_INPUT)
            self._password_input = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
            self._submit_button = self._driver.find_element(By.XPATH, self.SUBMIT_BUTTON)
        except c.NoSuchElementException as e:
            print("NoSuchElementException", e)

    def fill_user_name_input(self, user):
        self._user_name_input.send_key(user)

    def fill_password_input(self, password):
        self._password_input.send_key(password)

    def click_on_submit_button(self):
        self._submit_button.click()
