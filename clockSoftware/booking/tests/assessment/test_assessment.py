import pytest
from clockSoftware.booking.src.pages.HomePage import HomePage
from clockSoftware.booking.src.pages.RoomPage import RoomPage
from clockSoftware.booking.src.pages.ExtrasPage import ExtrasPage
from clockSoftware.booking.src.pages.CheckoutPage import CheckoutPage
from clockSoftware.booking.src.pages.PaymentPage import PaymentPage
from clockSoftware.booking.src.pages.ConfirmationPage import ConfirmationPage
import datetime
from clockSoftware.booking.src.helpers.BaseClass import  BaseClass
@pytest.mark.usefixtures('init_driver')
class TestAssessment(BaseClass):

    @pytest.mark.tcid01
    def test_assessment(self):
        log=self.getLogger()
        log.info("Test Log")
        home = HomePage(self.driver)
        room = RoomPage(self.driver)
        extras = ExtrasPage(self.driver)
        checkout = CheckoutPage(self.driver)
        payment = PaymentPage(self.driver)
        confirm = ConfirmationPage(self.driver)

        nights = 4

        home.go_to_home_page()

        home.click_date_field()

        home.click_date()

        home.input_nights(nights)

        home.click_book()

        expected_arrival = room.click_most_expensive_option()

        extras.input_cleaning()

        extras.input_fitness()

        extras.click_add()

        arrival_date = checkout.arrival()
        assert arrival_date == expected_arrival, 'The arrival date is not shown as expected'

        stay = checkout.stay()
        assert stay == str(nights), 'The number of stay is not shown as expected'

        departure_date = checkout.departure()
        assert departure_date == (datetime.datetime.strptime(expected_arrival, "%d %b %Y") + datetime.timedelta(
                        days=4)).strftime('%d %b %Y'), 'The departure date is not shown as expected'

        room_type = checkout.type()
        assert room_type == 'Deluxe Appartment', 'Room Type is not shown as expected'

        rate = checkout.rate()
        assert rate == 'Rack Rate Standard Max +', 'Rate is not shown as expected'

        extra_service_charge = checkout.extra()
        assert extra_service_charge == '6.00 EUR', 'Extra service charge is not shown as expected'

        total = checkout.total()
        assert total == '1,656.00 EUR', 'Total is not shown as expected'
        log
        checkout.email()

        checkout.last_name()

        checkout.first_name()

        checkout.phone()

        checkout.cc()

        checkout.agree()

        checkout.create()

        payment.cc_number()

        payment.brand()

        payment.visa()

        payment.exp_month()

        payment.month()

        payment.exp_year()

        payment.year()

        payment.address()

        payment.zip()

        payment.city()

        payment.state()

        payment.country()

        payment.afghanistan()

        payment.submit()

        confirmation = confirm.confirmation()
        assert confirmation == 'Thank you for your booking!', 'Confirmation message is not shown as expected'
