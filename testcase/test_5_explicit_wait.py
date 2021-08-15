import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.com/")
wait = WebDriverWait(driver, 2)


@pytest.mark.skip
def test_5_method1():
    elements = wait.until(EC.presence_of_all_elements_located((By.PARTIAL_LINK_TEXT, "cat")))
    assert True if elements else False, "Assertion Error #5.1 - element do not exist."


driver.close()
