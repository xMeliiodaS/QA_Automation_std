from selenium.webdriver.common.by import By

from infra.base_page import BasePage


class BasePageApp(BasePage):
    LOGO_IMAGE = '//img[@class="custm-logo"]'

    def __init__(self, driver):
        super().__init__(driver)
        self._logo_image = self._driver.find_element(By.XPATH, self.LOGO_IMAGE)

    def logo_is_displayed(self):
        return self._logo_image.is_displayed()
