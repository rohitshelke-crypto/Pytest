
##like suppose if you want to run your  test cases on different browser(like chrome or firefox) then this is one method but this bit long coding you have to do
###like need to create two classes and then it will initiate with fixtures
# in output you can see two browsers are opening ,first is chrome then firefox

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from webdriver_manager.firefox import GeckoDriverManager
import pytest


@pytest.fixture(scope='class')     ##defining Fixture
def init_chrome_driver(request):            ##defining method name and instead of creating global driver we are taking paraameter here that is request
    ch_driver=webdriver.Chrome(ChromeDriverManager().install())
    request.cls.driver=ch_driver     ##for the class level we are using driver and puting into in variale called ch_driver

    yield
    ch_driver.close()


@pytest.fixture(scope='class')
def init_ff_driver(request):
    ff_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    request.cls.driver = ff_driver

    yield
    time .sleep(5)
    ff_driver.close()

##in above we have created two fixtures
##in below creating base class for Chrome fixture

@pytest.mark.usefixtures('init_chrome_driver')       ##because of this fixture we can able to initialize driver
class Base_Chrome_Test:   ##This is blank class and its parent class
    pass

class Test_Google_Chrome(Base_Chrome_Test):  ##This is child class

    def test_google_title_chrome(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.title=="Google"




@pytest.mark.usefixtures('init_ff_driver')               #####because of this fixture we can able to initialize driver
class Base_ff_Test:   ##This is blank class and its parent class
    pass

class Test_Google_ff(Base_ff_Test):  ##This is child class

    def test_google_title_ff(self):
        self.driver.get("https://www.google.com/")
        assert self.driver.title=="Google"






