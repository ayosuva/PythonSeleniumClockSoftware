from selenium.webdriver.common.by import By

from clockSoftware.booking.src.helpers.ReusableFunctions import ReusableFunctions


class ConfirmationPage:
    CONFIRMATION = (By.XPATH, '//*[@id="top_position_container"]/div[2]/h1')

    def __init__(self, driver):
        self.driver = driver
        self.sl = ReusableFunctions(self.driver)

    def confirmation(self):
        confirmation = self.sl.wait_get_element(self.CONFIRMATION).text
        return confirmation
