import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("D:\Pliki\Git_repo\Selenium\chromedriver.exe")
driver.get("https://www.amazon.com/")

search = driver.find_element_by_id("twotabsearchtextbox")
search.send_keys("cvbatfcd")  # creation of unsuccesfull search page instance
search.send_keys(Keys.RETURN)

negsearch = driver.find_element_by_xpath("//span[@class = 'a-text-normal']").text


def test_2_method1():  # assertion to prove the unsuccesfull search page
    assert "Need help?" in negsearch, \
        "Assertion Error #2.1 - Negative search was unsuccesfull or assertion did not work" \
        " or arg type of WebElement is not iterable"


driver.close()
