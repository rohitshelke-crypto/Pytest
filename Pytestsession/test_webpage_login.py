##To run your test cases in parral mode then you have to install pip install pytest-xdist command
##without xdist command you cant run test cases parally

##Give this command to run your tst cases parally :::pytest -v -s Pytestsession/test_webpage_login.py -n 5
##here we are executing test cases parally


from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_google():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(5)
    driver.get("https://www.google.co.in/")
    assert driver.title=='Google'

    time.sleep(5)
    driver.quit()


def test_facebook():
    driver=webdriver.Chrome(executable_path="G:\Downloads\chromedriver_win32\chromedriver.exe")
    driver.implicitly_wait(5)
    driver.get("https://www.facebook.com/")
    assert driver.title=='Facebook – log in or sign up'
    driver.quit()


def test_insta():
    driver=webdriver.Chrome(executable_path="G:\Downloads\chromedriver_win32\chromedriver.exe")
    driver.implicitly_wait(5)
    driver.get("https://www.instagram.com/")
    assert driver.title=='Instagram'
    driver.quit()




