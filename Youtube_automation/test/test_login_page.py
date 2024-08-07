import time
import unittest
import undetected_chromedriver as uc
from infra.config_provider import ConfigProvider
from logic.home_page import HomePage
from logic.login_page import LoginPage


class TestLoginPage(unittest.TestCase):

    # Before all - Called automatically
    def setUp(self):
        # Initialize the undetected ChromeDriver
        options = uc.ChromeOptions()
        options.add_argument("--disable-blink-features=AutomationControlled")
        self.driver = uc.Chrome(options=options)
        self.config = ConfigProvider.load_config_json()
        self.driver.get(self.config["url"])
        self.home_page = HomePage(self.driver)

    def test_login_successful(self):
        # Wait for the page to load
        self.home_page.click_on_login_button()

        login_page = LoginPage(self.driver)
        login_page.fill_username_input(self.config["email"])
        login_page.click_on_next_button()

        login_page.fill_password_input(self.config["password"])
        login_page.click_on_next_button()


if __name__ == "__main__":
    unittest.main()
