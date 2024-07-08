import unittest

from infra.browser_wrapper import BrowserWrapper
from infra.config_provider import ConfigProvider
from infra.utils import Utils
from logic.login_page import LoginPage
from logic.main_page import MainPage


class TestLoginPage(unittest.TestCase):

    # Before all - Called automatically
    def setUp(self):
        self.browser = BrowserWrapper()
        self.config = ConfigProvider.load_config_json()
        self.driver = self.browser.get_driver(self.config["url"])
        self.login_page = LoginPage(self.driver)

    def tearDown(self):
        self.browser.close_browser()

    def test_login_successful(self):
        self.login_page.fill_user_name_input(self.config["user_name"])
        self.login_page.fill_password_input(self.config["password"])
        self.login_page.click_on_submit_button()

        main_page = MainPage(self.driver)
        self.assertTrue(main_page.login_title_is_displayed())

    def test_login_failed(self):
        self.login_page.fill_user_name_input(self.config["user_name"])
        self.login_page.fill_password_input(Utils.generate_random_string(8))
        #   self.login_page.fill_password_input(self.config["incorrect_password"])
        self.login_page.click_on_submit_button()

        main_page = MainPage(self.driver)
        self.assertFalse(main_page.login_title_is_displayed())
