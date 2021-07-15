import json
from selenium.webdriver.common.by import By

config = json.load(open("config.json"))


class Pushgateway:
    URL = config["pushgateway-url"]
    JENKINS_URL = config["jenkins-url"]
    JENKINS_USERNAME = config["jenkins-username"]
    JENKINS_PASSWORD = config["jenkins-password"]
    JENKINS_JOB = config["jenkins-job"]
    JOB_DESC = config["job-desc"]
    PRODUCT = config["product"]
    PRIORITY = config["priority"]


class StartPageLocators:
    URL =
    LOGIN_BUTTON = (
        By.XPATH, 
        '//div[contains(text(), "Войти через")]/b[contains(text(), "mos.ru")]/../..'
    )


class LoginPageLocators:
    LOGIN = config['mos_login']
    PASSWORD = config['mos_password']

    LOGIN_INPUT = (By.CSS_SELECTOR, 'input#login')
    PASSWORD_INPUT = (By.CSS_SELECTOR, 'input#password')
    LOGIN_BUTTON = (By.CSS_SELECTOR, 'button#bind')


class MainPageLocators:
    LOGOUT_BUTTON = (
        By.XPATH,
        '//button[contains(@class, "client-profile_exit")]'
    )

    EMPLOYEE_ACTIVE_ROLE = (
        By.XPATH, 
        '//div[contains(text(), "Сотрудник") and contains(@class, "is-active")]'
    )

    PARENT_ROLE = (
        By.XPATH,
        '//div[contains(text(), "Родитель")]'
    )
    PORTFOLIO_BUTTON = (
        By.XPATH,
        '//div[contains(@class, "service-portfolio")]//button[contains(text(), "Перейти")]'
    )


class PortfolioLocators:
    USER_INFO_BUTTON = (
        By.XPATH,
        '//div[contains(@class, "current-user-info")]/button'
    )

    LOGOUT_BUTTON = (
        By.XPATH,
        '//div[contains(@class, "user-actions-menu")]/li/span[contains(text(), "Выйти")]'
    )