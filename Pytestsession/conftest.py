

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from webdriver_manager.firefox import GeckoDriverManager
import pytest

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


