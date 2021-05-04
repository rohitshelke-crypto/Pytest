'''
how to create fixtures for different browsers like chrome, Firefox using parameters
how to pass fixture params
Run test cases in parallel mode
generate html reports with fixtures


'''



##here we are using param keyword in fixtures using that we dont neeed to create two classes for two browsers with the help of param keyword we can initialize two browsers within one fixture
##like with the help of this param your code will be less and you can execute the test cases with multiple browsers

##you cal aslo do the parallal execution(.....-n 4)

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from webdriver_manager.firefox import GeckoDriverManager
import pytest

''''
we have use conftest.py  file and through that this file id getting executed 

@pytest.fixture(params=['chrome','firefox'],scope='class')   ##defining two browser using param
def init_driver(request):
    if request.param=='chrome':
        web_driver=webdriver.Chrome(ChromeDriverManager().install())
        request.cls.driver = web_driver


    if request.param=='firefox':
        web_driver=webdriver.Firefox(executable_path=GeckoDriverManager().install())
        request.cls.driver=web_driver
    yield
    web_driver.close()
'''

@pytest.mark.usefixtures('init_driver')
class BaseTest:
    pass

class Test_Google_title(BaseTest):
    def test_google_title(self):
        self.driver.get("https://www.google.com/")
        self.driver.title=="Google"



