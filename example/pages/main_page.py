import pytest

from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage
from pages.locators import MainPageLocators, PortfolioLocators


class MainPage(BasePage):
    def open_portfolio(self):
        try:
            self.browser.find_element(*MainPageLocators.PARENT_ROLE).click()
            self.wait_until_element_displayed(*MainPageLocators.PORTFOLIO_BUTTON, 30)
        except TimeoutException:
            pytest.fail('Не найдена ссылка на портфолио')

        try:
            self.wait_until_element_is_clickable(*MainPageLocators.PORTFOLIO_BUTTON, 30)
            self.browser.find_element(*MainPageLocators.PORTFOLIO_BUTTON).click()
            self.wait_until_element_displayed(*PortfolioLocators.USER_INFO_BUTTON, 30)
        except TimeoutException:
            pytest.fail('Не удалось перейти в портфолио')