from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import time


class ReusableFunctions:

    def __init__(self, driver):
        self.driver = driver
        self.default_timeout = 30

    def wait_and_click(self, locator, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).click()
        except StaleElementReferenceException:
            time.sleep(2)
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            ).click()

    def wait_and_input_text(self, locator, text, timeout=None):
        timeout = timeout if timeout else self.default_timeout

        clickable = WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )
        clickable.click()
        clickable.send_keys(Keys.CONTROL + 'a')
        clickable.send_keys(Keys.BACK_SPACE)
        clickable.send_keys(text)

    def wait_get_element(self, locator, timeout=None, err=None):
        timeout = timeout if timeout else self.default_timeout
        err = err if err else f'Unable to find elemnets located by "{locator}", after timeout of {timeout}'
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(err)

        return element

    def wait_get_elements(self, locator, timeout=None, err=None):
        timeout = timeout if timeout else self.default_timeout
        err = err if err else f'Unable to find elemnets located by "{locator}", after timeout of {timeout}'
        try:
            elements = WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located(locator)
            )
        except TimeoutException:
            raise TimeoutException(err)

        return elements
