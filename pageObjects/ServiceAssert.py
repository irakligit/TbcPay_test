from selenium.webdriver.common.by import By
from dataObjects.LocatorsData import Header
from pageObjects.AssertionLogic import CheckElements
from pageObjects.Screenshot import ScreenShot
import allure


class ServicePage(object):

    def __init__(self, driver):
        self.driver = driver

    @allure.step("Find service elements")
    def serviceElements(self):
        screenshot = ScreenShot(self.driver)
        self.popularuli_servisebi = self.driver.find_element(By.XPATH, Header.popularuli_servisebi)
        self.mobiluri_kavshiri = self.driver.find_element(By.XPATH, Header.mobiluri_kavshiri)
        self.bankebi_dazgveva_mikrosafinanso = self.driver.find_element(By.XPATH, Header.bankebi_dazgveva_mikrosafinanso)
        self.totalizatorebi_kazino_lataria = self.driver.find_element(By.XPATH, Header.totalizatorebi_kazino_lataria)
        self.interneti_telefoni_televizia = self.driver.find_element(By.XPATH, Header.interneti_telefoni_televizia)
        self.komunaluri_gadasaxadebi = self.driver.find_element(By.XPATH, Header.komunaluri_gadasaxadebi)
        self.transporti = self.driver.find_element(By.XPATH, Header.transporti)
        self.saxelmwifo_servisebi = self.driver.find_element(By.XPATH, Header.saxelmwifo_servisebi)
        self.sxvadasxva = self.driver.find_element(By.XPATH, Header.sxvadasxva)
        self.search = self.driver.find_element(By.NAME, Header.search)
        screenshot.screen()


    @allure.step("Assertion of service elements")
    def serviceAssertion(self):
        screenshot = ScreenShot(self.driver)
        CheckElements.check_locator_exists(self.popularuli_servisebi)
        CheckElements.check_locator_exists(self.mobiluri_kavshiri)
        CheckElements.check_locator_exists(self.bankebi_dazgveva_mikrosafinanso)
        CheckElements.check_locator_exists(self.totalizatorebi_kazino_lataria)
        CheckElements.check_locator_exists(self.interneti_telefoni_televizia)
        CheckElements.check_locator_exists(self.komunaluri_gadasaxadebi)
        CheckElements.check_locator_exists(self.transporti)
        CheckElements.check_locator_exists(self.saxelmwifo_servisebi)
        CheckElements.check_locator_exists(self.sxvadasxva)
        #საძიებო ველი
        CheckElements.check_locator_exists(self.search)
        screenshot.screen()









