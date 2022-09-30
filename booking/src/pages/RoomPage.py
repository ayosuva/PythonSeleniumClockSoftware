import datetime
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait

from booking.src.helpers.ReusableFunctions import ReusableFunctions
from selenium.webdriver.common.by import By


class RoomPage:
    label_room_types = (By.XPATH, '//div[contains(@class,"bookable-container bookable-location")]//h2')
    btn_Check_availability_calendar = (By.XPATH, '//a[contains(text(),"Check availability calendar")]')
    label_Dates = (By.XPATH,
                   '//h4[contains(text(),"Deluxe Appartment")]/../../following-sibling::div[1]//a[contains(@class,'
                   '"list-group-item list-group-item")]')
    btn_Next_Page = (By.XPATH, '//div[@class="icon-double-angle-right"]')
    btn_search_For_Available_Rooms = (By.XPATH, '//input[@value="Search for available rooms"]')
    label_selected_Date = (By.XPATH, '//div[@class="h2 text-center"]')
    label_price = (By.XPATH,
                   '//h2[contains(text(),"Deluxe Appartment")]/../../following-sibling::div[1]//tr['
                   '@class="room-type"]//td[@class="text-right hidden-xs"]//*[contains(text(),"EUR")]')
    btn_Select = (By.XPATH, '//span[@class="pull-right"]//a[@class="btn btn-success "]//i')
    By
    label_from_date_period = (By.XPATH, '//input[@id="form_period_from_date"]')
    highest_value = 0
    iframe_id = 'clock_pms_iframe_1'

    def __init__(self, driver):
        self.driver = driver
        self.sl = ReusableFunctions(self.driver)

    def click_most_expensive_option(self):
        self.driver.switch_to.frame(self.iframe_id)
        room_types = self.sl.wait_get_elements(self.label_room_types)
        available_room_types = ''
        date = ''
        for room_type in room_types:
            available_room_types = available_room_types + ' ' + room_type.text

        if 'Deluxe Appartment' not in available_room_types:
            self.sl.wait_get_element(self.btn_Check_availability_calendar).click()
            numberOfNights = 0
            list_dates_availability = []
            while numberOfNights <= 3:
                list_dates_availability = self.sl.wait_get_elements(self.label_Dates)
                for i in range(len(list_dates_availability)):
                    class_attribute = list_dates_availability[i].get_attribute("class")
                    if 'danger' in class_attribute:
                        numberOfNights = 0
                    else:
                        numberOfNights += 1
                    if numberOfNights == 4:
                        list_dates_availability[i - 3].click();
                        break
                if numberOfNights != 4:
                    current_Date = self.sl.wait_get_element(self.label_from_date_period).get_attribute("value")
                    next_date = (datetime.datetime.strptime(current_Date, "%d %b %Y") + datetime.timedelta(
                        days=12)).strftime('%d %b %Y')
                    self.sl.wait_get_element(self.btn_Next_Page).click()
                    wait = WebDriverWait(self.sl.driver, timeout=10, poll_frequency=1,
                                         ignored_exceptions=[StaleElementReferenceException])
                    element = wait.until(
                        EC.text_to_be_present_in_element_attribute(self.label_from_date_period, "value", next_date))
                else:
                    self.sl.wait_get_element(self.btn_search_For_Available_Rooms).click()
                    break
                numberOfNights = 0
            date = self.select_Highest_Price_Deluxe_Apartment()

        else:
            date = self.select_Highest_Price_Deluxe_Apartment()

        return date

    def select_Highest_Price_Deluxe_Apartment(self):
        arrival_date = self.sl.wait_get_element(self.label_selected_Date).text
        date = (datetime.datetime.strptime(arrival_date.split(' - ')[0], "%d %b %Y")).strftime('%d %b %Y')
        list_prices = self.sl.wait_get_elements(self.label_price)
        list_prices_values = [None] * len(list_prices)
        for i in range(len(list_prices)):
            list_prices_values[i] = list_prices[i].accessible_name.split(" ")[0].replace(",", "")

        highest_value = max(list_prices_values)
        list_select_button = self.sl.wait_get_elements(self.btn_Select)
        for i in range(len(list_prices)):
            if list_prices[i].accessible_name.split(" ")[0].replace(",", "") == max(list_prices_values):
                list_select_button[i].click()

        return date
