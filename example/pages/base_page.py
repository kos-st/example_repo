from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        print(f"Переход на {self.url}")
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_element_enabled(self, how, what):
        return self.browser.find_element(how, what).is_enabled()

    def wait_until_element_displayed(self, how, what, timeout=4):
        WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located((how, what))
        )

    def wait_until_element_present(self, how, what, timeout=4):
        WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located((how, what))
        )

    def wait_until_element_is_clickable(self, how, what, timeout=4):
        WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable((how, what))
        )

    def wait_until_element_disappear(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, 4).until(EC.presence_of_element_located((how, what)))
            WebDriverWait(self.browser, timeout).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            pass
