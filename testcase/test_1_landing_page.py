import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.com/")

title = driver.title
strtest = "DVDs"


def test_1_method1():
    assert strtest in title, "Assertion Error #1.1 - String is not a substring of a title."


footer = driver.find_elements_by_id("navFooter")
lenfoot = len(footer)


def test_1_method2():  # checks if there is a footer by creating a list from len
    assert lenfoot > 0, "Assertion Error #1.2 - Footer does not exist."


driver.close()
