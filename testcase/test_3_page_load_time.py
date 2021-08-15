# I found most of it on the web with PerformanceTiming web API, and think it's neat.
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.amazon.com/")

navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
responseStart = driver.execute_script("return window.performance.timing.responseStart")
domComplete = driver.execute_script("return window.performance.timing.domComplete")

backendPerformance_calc = responseStart - navigationStart
frontendPerformance_calc = domComplete - responseStart


def test_3_method1():
    assert backendPerformance_calc <= 500 and frontendPerformance_calc <= 3000, \
        "Assertion Error #3.1 - loading the page took too long."


driver.close()
