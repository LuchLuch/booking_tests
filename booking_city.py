import unittest
import random
import time
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





today_day = date.today().day

class Sum_Kids(unittest.TestCase):
    def setUp(self):
        # Choose Chrome or Firefox
        # self.driver = webdriver.Firefox(executable_path=r'./geckodriver')
        self.driver = webdriver.Chrome(executable_path=r"./chromedriver")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('http://booking.com/')
        self.assertIn('Booking.com', self.driver.title)



    def test_city_hotel(self):
        # search for random city and press
        self.cities = self.driver.find_elements_by_class_name('promotion-postcard__small')
        self.driver.implicitly_wait(10)
        self.random_city = (random.choice(self.cities)).click()
        self.hotels = self.driver.find_elements_by_class_name('bui-price-display__value.prco-inline-block-maker-helper')
        self.assertIsNotNone(self.hotels!=None, "The price element  is here") # Check - no result entry containing booking price or booking status

        # wait elements
        self.element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "no_dates_click.jq_tooltip")))

        # Click "show prices" button for any hotel
        self.hotels = self.driver.find_elements_by_class_name('no_dates_click.jq_tooltip')
        self.driver.implicitly_wait(10)
        self.random_city = (random.choice(self.hotels)).click()
        time.sleep(5)

        # Set any dates for check in and out
        self.choose_day = self.driver.find_elements_by_xpath('//*[@id="frm"]//table/tbody/tr/td')
        self.choose_day[today_day+5].click()

        #Submit search form
        time.sleep(5)
        self.search_button = self.driver.find_element_by_xpath('//*[@id="frm"]/div/div/button').click()




    def tearDown(self):
        # close the browser window
        self.driver.quit()





if __name__ == '__main__':
    unittest.main()