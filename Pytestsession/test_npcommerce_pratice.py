
##Not able to take a screenshots and how to create oabject for a class and in unit testing also
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


@pytest.mark.usefixtures('init_driver')
class BaseTest:
    pass

class Test_Google_title(BaseTest):

    def test_google_title(self):

        self.driver.get("https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F")
        email = self.driver.find_element_by_xpath(
            "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[1]/input")
        email.clear()
        time.sleep(2)
        email.send_keys("admin@yourstore.com")
        pwd = self.driver.find_element_by_xpath(
            "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[2]/div[2]/input")
        pwd.clear()
        pwd.send_keys('admin')
        self.driver.maximize_window()

        self.driver.find_element_by_id("RememberMe").click()
        self.driver.find_element_by_xpath(
            "/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
        print(self.driver.title)
        title = "Dashboard / nopCommerce administration"

        if title == "Dashboard / nopCommerce administration":
            print("title is correct")
        else:
            print("wrrong title")
            #self.driver.save_screenshot("F:\\All_About_Pytest\\Screenshots" + "test_google_title.png")
            self.driver.save_screenshot("G:\\HOLLYWOOD_MOVIES\\test_google_title.png")
            self.obj_bird = BaseTest()
            obj_parr=Test_Google_title()
            obj_parr.test_google_title()

#self.s1 = Test_Google_title()
#self.s1.test_google_title



#self.driver.find_element_by_xpath("/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/a/p").click()
#self.driver.find_element_by_xpath("/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[2]/ul/li[1]/a").click()





