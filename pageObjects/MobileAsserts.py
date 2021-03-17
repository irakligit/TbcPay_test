from selenium import webdriver
from selenium.webdriver.common.by import By
from dataObjects.LocatorsData import Header
from pageObjects.AssertionLogic import CheckElements
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pageObjects.Screenshot import ScreenShot
import allure


class MobilePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)







    @allure.step("Field actions")
    def field_actions(self):
        screenshot = ScreenShot(self.driver)
        self.search = self.driver.find_element(By.NAME, Header.search)
        #საძიებო ველის არსებობის შემოწმება
        if CheckElements.check_locator_exists(self.search):
            self.search.send_keys("მობილური")
        #ბალანსის შევსების არსებობის შემოწმება
        self.balansis_shevseba = self.driver.find_element(By.XPATH, Header.balansis_shevseba)
        if CheckElements.check_locator_exists(self.balansis_shevseba):
            self.balansis_shevseba.click()
        screenshot.screen()



    @allure.step("enter and check mobile number")
    def number_actions(self):
        screenshot = ScreenShot(self.driver)
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, Header.number_element)))
        self.number = self.driver.find_element(By.CLASS_NAME, Header.number_element)
        if CheckElements.check_locator_exists(self.number):
            self.number.send_keys("555122334")
        self.shemowmeba = self.driver.find_element(By.XPATH, Header.shemowmeba)
        if CheckElements.check_locator_exists(self.shemowmeba):
            self.shemowmeba.click()
        screenshot.screen()

    @allure.step("Various actions on elements")
    def dropdown(self):
        screenshot = ScreenShot(self.driver)
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, Header.airchiet_servisi)))
        self.airchiet_servisi = self.driver.find_element(By.CSS_SELECTOR, Header.airchiet_servisi)
        self.airchiet_servisi.click()
        dropdown_balansi = self.driver.find_element(By.CSS_SELECTOR, Header.dropdown_balansi)
        CheckElements.check_locator_exists(dropdown_balansi)
        meti_8 = self.driver.find_element(By.XPATH, Header.meti_8)
        CheckElements.check_locator_exists(meti_8)
        meti_10 = self.driver.find_element(By.XPATH, Header.meti_10)
        CheckElements.check_locator_exists(meti_10)
        meti_10.click()
        screenshot.screen()













