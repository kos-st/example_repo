import pytest
import time

from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage
from pages.locators import PortfolioLocators, StartPageLocators


class PortfolioPage(BasePage):
    def logout(self):
        try:
            self.browser.find_element(*PortfolioLocators.USER_INFO_BUTTON).click()
            self.wait_until_element_displayed(*PortfolioLocators.LOGOUT_BUTTON, 30)
            time.sleep(0.5)
            self.browser.find_element(*PortfolioLocators.LOGOUT_BUTTON).click()
        except TimeoutException:
            pytest.fail('Не найдена кнопка выхода')
        
        try:
            self.wait_until_element_displayed(*StartPageLocators.LOGIN_BUTTON, 30)
        except TimeoutException:
            pytest.fail('Выход к посадочной странице не выполнен')