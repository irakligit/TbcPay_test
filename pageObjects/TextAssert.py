from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from dataObjects.LocatorsData import Header
from pageObjects.AssertionLogic import CheckElements
from pageObjects.Screenshot import ScreenShot
import allure


class TextAssert(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)
    #მეტი - ლ ღილაკზე დაჭერის შემდგომ ელემენტების ტექსტების არსებობა მოწმდება აქ

    @allure.step("Assertion of elements texts")
    def asserts(self):
        screenshot = ScreenShot(self.driver)
        self.wait.until(EC.visibility_of_element_located((By.XPATH, Header.spanElement)))
        spanElements = self.driver.find_elements_by_xpath("//div[@class='ded17e-0 iiRqkB']//span")
        empty_list = []
        for i in range(len(spanElements)):
            empty_list.insert(i, spanElements[i].text)
        list = ["დავალიანება", "c", "თანხის ოდენობა", "c",
                         "საკომისიო", "0.12",
                         "c", "ჯამში გადასახდელი",
                         "c", "გადახდა", "სხვა გადახდის დამატება"]
        first = set(empty_list)
        second = set(list)
        assert first == second, "fail"

        ten_lari = self.driver.find_element(By.CLASS_NAME, Header.ten_lari)
        CheckElements.check_text_exists(ten_lari, "10.00 c")

        value_10 = self.driver.find_element(By.XPATH, Header.value_10)
        CheckElements.check_locator_exists(value_10)

        info = self.driver.find_element(By.XPATH, Header.info)
        CheckElements.check_text_exists(info, "10.12 c")
        payBtn = self.driver.find_element(By.CLASS_NAME, Header.payBTN)
        CheckElements.check_locator_exists(payBtn)
        payBtn.click()
        self.wait.until(EC.invisibility_of_element(payBtn))
        screenshot.screen()







