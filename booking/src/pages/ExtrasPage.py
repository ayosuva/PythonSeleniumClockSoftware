from selenium.webdriver.common.by import By

from booking.src.helpers.ReusableFunctions import ReusableFunctions

class ExtrasPage:

    CLEANING = (By.XPATH, '//div[4]/div/div/div[2]/div/div[3]/input')
    FITNESS = (By.XPATH, '//div[5]/div/div/div[2]/div/div[3]/input')

    ADD_EXTRAS_BTN = (By.XPATH, '//div[6]/div/span/input')

    def __init__(self, driver):
        self.driver = driver
        self.sl = ReusableFunctions(self.driver)

    def input_cleaning(self, number='1'):
        self.sl.wait_and_input_text(self.CLEANING, number)

    def input_fitness(self, number='1'):
        self.sl.wait_and_input_text(self.FITNESS, number)

    def click_add(self):
        self.sl.wait_and_click(self.ADD_EXTRAS_BTN)
