from selenium.webdriver.common.by import By

from clockSoftware.booking.src.helpers.ReusableFunctions import ReusableFunctions
from clockSoftware.booking.src.helpers.generic_helpers import generate_random_email_and_password
from clockSoftware.booking.src.pages.HomePage import HomePage

class CheckoutPage:
    ARRIVAL = (By.XPATH, '//*[@id="top_position_container"]/div[3]/div[3]/div[1]/div[2]/div[1]/div[2]')

    STAY = (By.XPATH, '//*[@id="top_position_container"]/div[3]/div[3]/div[1]/div[2]/div[2]/div[2]')

    DEPARTURE = (By.XPATH, '//*[@id="top_position_container"]/div[3]/div[3]/div[1]/div[2]/div[3]/div[2]')

    TYPE = (By.XPATH, '//*[@id="top_position_container"]/div[3]/div[3]/div[1]/div[2]/div[5]/div[2]')

    RATE = (By.XPATH, '//*[@id="top_position_container"]/div[3]/div[3]/div[1]/div[2]/div[6]/div[2]')

    EXTRAS = (By.XPATH, '//*[@id="top_position_container"]/div[3]/div[3]/div[1]/div[2]/div[9]/div[2]')

    TOTAL = (By.XPATH, '//*[@id="top_position_container"]/div[3]/div[3]/div[1]/div[2]/div[11]/div[2]/h3')

    EMAIL = (By.XPATH, '//*[@id="booking_guest_attributes_e_mail"]')

    LAST_NAME = (By.XPATH, '//*[@id="booking_guest_attributes_last_name"]')

    FIRST_NAME = (By.XPATH, '//*[@id="booking_guest_attributes_first_name"]')

    PHONE = (By.XPATH, '//*[@id="booking_guest_attributes_phone_number"]')

    CC = (By.XPATH, '//*[@id="booking_payment_service_credit_card_collect"]')

    AGREE = (By.XPATH, '//*[@id="booking_agreed"]')

    CREATE = (By.XPATH, '//*[@id="new_booking"]/div[5]/div[2]/div[3]/input')
    def __init__(self, driver):
        self.driver = driver
        self.sl = ReusableFunctions(self.driver)

    def arrival(self):
        arrival = self.sl.wait_get_element(self.ARRIVAL).text
        #print(HomePage.entered_date) global variable example
        return arrival

    def stay(self):
        stay = self.sl.wait_get_element(self.STAY).text
        return stay

    def departure(self):
        departure = self.sl.wait_get_element(self.DEPARTURE).text
        return departure

    def type(self):
        type = self.sl.wait_get_element(self.TYPE).text
        return type

    def rate(self):
        rate = self.sl.wait_get_element(self.RATE).text
        return rate

    def extra(self):
        extra = self.sl.wait_get_element(self.EXTRAS).text
        return extra

    def total(self):
        total = self.sl.wait_get_element(self.TOTAL).text
        return total

    def email(self, email=None):
        if not email:
            rand_email = generate_random_email_and_password()
            email = rand_email['email']
        self.sl.wait_and_input_text(self.EMAIL, email)

    def last_name(self, last_name=None):
        last_name = last_name if last_name else 'TestLastName'
        self.sl.wait_and_input_text(self.LAST_NAME, last_name)

    def first_name(self, first_name=None):
        first_name = first_name if first_name else 'TestFirstName'
        self.sl.wait_and_input_text(self.FIRST_NAME, first_name)

    def phone(self, phone=None):
        phone = phone if phone else '0000000000'
        self.sl.wait_and_input_text(self.PHONE, phone)

    def cc(self):
        self.sl.wait_and_click(self.CC)

    def agree(self):
        self.sl.wait_and_click(self.AGREE)

    def create(self):
        self.sl.wait_and_click(self.CREATE)