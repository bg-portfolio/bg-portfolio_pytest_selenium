from selenium.webdriver.common.keys import Keys


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    def type_search(self, text):
        return self.driver.find_element_by_name('g').send_keys(text)

    def type_enter(self):
        return self.driver.find_element_by_name('g').send_keys(Keys.ENTER)
