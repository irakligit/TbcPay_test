from selenium.webdriver.common.by import By
from dataObjects.LocatorsData import Header
from pageObjects.AssertionLogic import CheckElements
from pageObjects.Screenshot import ScreenShot
import allure



class HeaderPage(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Find header elements")
    def headerElements(self):
        screenshot = ScreenShot(self.driver)
        self.services = self.driver.find_element(By.XPATH, Header.services)
        self.transfers = self.driver.find_element(By.XPATH, Header.transfers)
        self.for_business = self.driver.find_element(By.XPATH, Header.for_business)
        self.foreign_payments = self.driver.find_element(By.XPATH, Header.foreign_payments)
        screenshot.screen()



    @allure.step("Assertion of header elements")
    def HeaderAssert(self):
        screenshot = ScreenShot(self.driver)
        CheckElements.check_locator_exists(self.services)
        CheckElements.check_locator_exists(self.transfers)
        CheckElements.check_locator_exists(self.for_business)
        CheckElements.check_locator_exists(self.foreign_payments)
        screenshot.screen()











