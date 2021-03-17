import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from pageObjects.HeaderAssert import HeaderPage
from pageObjects.ServiceAssert import ServicePage
from pageObjects.MobileAsserts import MobilePage
from pageObjects.TextAssert import TextAssert
import pytest
import allure
from time import sleep


#დავალება დავწერე page object model ის გამოყენებით



@allure.epic("tbcpay_test")
@allure.feature("page object model")
@allure.severity(allure.severity_level.NORMAL)
class MainTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("https://tbcpay.ge/")


    #დავალების პირველი ნაწილი რომელიც მოიცავს სერვისების და ჰედერის ელემენტების შემოწმებას
    @allure.description("Services and header assertion test")
    def test_2(self):
        headerpage = HeaderPage(self.driver)
        servicepage = ServicePage(self.driver)
        headerpage.headerElements()
        headerpage.HeaderAssert()
        servicepage.serviceElements()
        servicepage.serviceAssertion()

    #დავალების მეორე ნაწილი რომელიც მოიცავს დარჩენილ ნაწილს
    @allure.description("Part Two: Actions on Elements")
    def test_1(self):
        mobile = MobilePage(self.driver)
        textassert = TextAssert(self.driver)
        mobile.field_actions()
        mobile.number_actions()
        mobile.dropdown()
        textassert.asserts()
        if "ecommerce.ufc.ge" in self.driver.current_url:
            print("ecommerce.ufc.ge is open")



    def tearDown(self):
        self.driver.close()



if __name__ == "__main__":
    unittest.main()
