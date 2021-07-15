import pytest

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

from pages.base_page import BasePage
from pages.locators import LoginPageLocators, MainPageLocators


class LoginPage(BasePage):
    def authorize(self):
        try:
            self.wait_until_element_is_clickable(*LoginPageLocators.LOGIN_BUTTON, 30)
            self.browser.find_element(
                *LoginPageLocators.LOGIN_INPUT
            ).send_keys(LoginPageLocators.LOGIN)
            self.browser.find_element(
                *LoginPageLocators.PASSWORD_INPUT
            ).send_keys(LoginPageLocators.PASSWORD, Keys.ENTER)
            self.wait_until_element_displayed(*MainPageLocators.LOGOUT_BUTTON, 30)
        except TimeoutException:
            pytest.fail('Не удалось авторизоваться')

        try:
            self.wait_until_element_displayed(*MainPageLocators.EMPLOYEE_ACTIVE_ROLE, 30)
        except TimeoutException:
            pytest.fail('Не выбрана роль "Сотрудник"')

