
import pytest
from booking.src.pages.HomePage import HomePage
from booking.src.pages.RoomPage import RoomPage
from booking.src.pages.ExtrasPage import ExtrasPage
from booking.src.pages.CheckoutPage import CheckoutPage
from booking.src.pages.PaymentPage import PaymentPage
from booking.src.pages.ConfirmationPage import ConfirmationPage

@pytest.mark.usefixtures('init_driver')
class TestAssessment:

    @pytest.mark.tcid01
    def test_assessment(self):

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

        expected_arrival=room.click_most_expensive_option()

        extras.input_cleaning()

        extras.input_fitness()

        extras.click_add()

        arrival = checkout.arrival()
        assert arrival == expected_arrival, 'Wrong'

        stay = checkout.stay()
        assert stay == str(nights), 'Wrong'

        #departure = checkout.departure()
        #assert departure == '14 Sep 2022', 'Wrong'

        type = checkout.type()
        assert type == 'Deluxe Appartment', 'Wrong'

        rate = checkout.rate()
        assert rate == 'Rack Rate Standard Max +', 'Wrong'

        extra = checkout.extra()
        assert extra == '6.00 EUR', 'Wrong'

        total = checkout.total()
        assert total == '1,656.00 EUR', 'Wrong'

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
        assert confirmation == 'Thank you for your booking!', 'Wrong'