import unittest

from selenium import webdriver


class FirstWebDriverTest(unittest.TestCase):

    def set_up(self):

        self.driver = webdriver.Chrome()

        self.driver.get("http://www.allegro.pl")

        self.SEARCH_TEXT = "Laptop"

        self.SEARCH_FIELD_ID = "//input[@id='main-search-text']"

        self.SEARCH_BUTTON_ID = "//input[@class='search-btn']"

        self.SEARCH_RESULT_ITEM_TITLE = "//article[@class='offer offer-brand']//h2//span"



def test_search_in_allegro_pl(self):

    driver = self.driver

    driver.find_element_by_xpath(self.SEARCH_FIELD_ID) \
.send_keys(self.SEARCH_TEXT)

    search_button = driver.find_element_by_xpath(self.SEARCH_BUTTON_ID)

    search_button.submit()

    driver.implicitly_wait(5000)

    result = driver.find_elements_by_xpath(self.SEARCH_RESULT_ITEM_TITLE).__getitem__(0).__getattribute__("text")

    self.assertIn(self.SEARCH_TEXT, result)

def tear_down(self):

    self.driver.close()
