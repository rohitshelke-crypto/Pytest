##we dont need to write setup method or tearddwn method sepretly directly using pytest fixture we can execute


#with below commmand we can also create html report using ficture
#pytest -v -s F:\All_About_Pytest\Pytestsession\test_pytest_fixture.py --html=creating_fixture_html_report.html



from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pytest
import test_pytest_fixture_html_report


driver = None  ##global variable

@pytest.fixture(scope='module')
def init_driver():


    global driver
    print("*************setup**********")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get('https://www.google.co.in/')

   ##Upto above coode will execute before the test case

    ##yield means it will execute after all test cases.

    yield
    print("*************Tear down*************")
    driver.quit()

def test_google_title(init_driver):
    assert driver.title == "Google"

def test_google_url(init_driver):
    assert driver.current_url == "https://www.google.co.in/"
