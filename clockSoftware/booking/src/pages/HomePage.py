
from selenium.webdriver.common.by import By
from clockSoftware.booking.src.helpers.config_helpers import get_base_url
from clockSoftware.booking.src.helpers.ReusableFunctions import ReusableFunctions
from datetime import datetime
class HomePage:

    DATE_FIELD = (By.ID, 'date-start')
    input_Arrival_Date = (By.XPATH, "//input[@id='date-start']")

    NIGHTS = (By.ID, 'to-place')

    BOOK_BTN = (By.XPATH, '//*[@id="flights"]/form/div/div[5]/input')
    entered_date=""
    def __init__(self, driver):
        self.driver = driver
        self.sl = ReusableFunctions(self.driver)

    def go_to_home_page(self):
        home_url = get_base_url()
        self.driver.get(home_url)

    def click_date_field(self):
        self.sl.wait_and_click(self.DATE_FIELD)

    def click_date(self):
        HomePage.entered_date=datetime.today().strftime('%d-%m-%Y')
        self.sl.wait_and_input_text(self.input_Arrival_Date,datetime.today().strftime('%d-%m-%Y'))

    def input_nights(self, nights=None):
        self.sl.wait_and_input_text(self.NIGHTS, nights)

    def click_book(self):
        self.sl.wait_and_click(self.BOOK_BTN)