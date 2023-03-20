from selenium import webdriver
import booking.constants as const


class Booking(webdriver.Firefox):
    def __init__(self, driver_path=r"C:\SeleniumDrivers"):
        self.driver_pat= driver_path
        super(Booking, self).__init__()

    def land_first_page(self):
        self.get(const.BASE_URL)