from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = True
options.page_load_strategy = 'normal'
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
# Could use os.getcwd() + \driver.exe for automated path finding.
driver.get("https://www.google.com")
accept = driver.find_element_by_id("gsr")
accept.click()

driver.save_screenshot("./test_6_headless_image.png")

driver.close()
