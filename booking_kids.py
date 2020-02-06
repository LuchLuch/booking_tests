import time
import unittest
from selenium import webdriver
import random


class Sum_Kids(unittest.TestCase):
    def setUp(self):
        # Choose Chrome or Firefox
        self.driver = webdriver.Firefox(executable_path=r'./geckodriver')
        # self.driver = webdriver.Chrome(executable_path=r"./chromedriver")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get('http://booking.com/')

    def test_count_fields(self):
        # open menu for selecting strangers number
        self.search_field = self.driver.find_element_by_class_name('xp__guests').click()
        self.driver.implicitly_wait(30)

        # specify N number of children (N > 1)
        self.number_of_children = random.randrange(1,5)
        self.count = self.driver.find_elements_by_class_name('bui-stepper__add-button')
        for i in range(self.number_of_children):
            self.count[1].click()
        self.driver.implicitly_wait(30)
        self.search = self.driver.find_elements_by_xpath('//*[@name="age"]')
        # Is the number of children equal to the number of input fields "age"?
        self.assertEqual(self.number_of_children, len(self.search))

    def tearDown(self):
        # close the browser window
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


