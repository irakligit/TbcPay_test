from selenium import webdriver
import allure

class ScreenShot(object):
    def __init__(self, driver):
        self.driver = driver

    def screen(self):
        allure.attach(self.driver.get_screenshot_as_png(), name="step screenshot",
                      attachment_type=allure.attachment_type.PNG)