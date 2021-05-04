##here we are creating html report using pytest
##give this command pytest -v -s F:\All_About_Pytest\test_pytest_fixture_html_report.py --html==creating_html_report.html
##and you can see the html report file in list and open that with firefox browser



from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest

driver = None  ##global variable

def setUpModule():

    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.delete_all_cookies()
    driver.get('https://www.google.co.in/')
    print(driver.current_url)

def tearDownModule():           ##driven will quit at the end because of this command
    driver.quit()


def test_google_title():
    assert driver.title == "Google"





def test_google_url():
    assert driver.current_url == "https://www.google.co.in/"
