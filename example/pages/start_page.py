import pytest

from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage
from pages.locators import StartPageLocators, LoginPageLocators


class StartPage(BasePage):
    def open_login_page(self):
        try:
            self.wait_until_element_displayed(*StartPageLocators.LOGIN_BUTTON, 30)
            self.browser.find_element(*StartPageLocators.LOGIN_BUTTON).click()
            self.wait_until_element_displayed(*LoginPageLocators.LOGIN_INPUT, 30)
        except TimeoutException:
            pytest.fail('Страница входа недоступна')
