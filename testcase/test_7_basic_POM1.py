from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from PageObjects1.google import HomePage


class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(3)
        self.base_url = "https://www.google.com/"

    def test_google_search(self):
        driver = self.driver
        driver.get(self.base_url)
        homepage = HomePage(driver)
        homepage.type_search("fley fawkes")
        homepage.type_enter()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
