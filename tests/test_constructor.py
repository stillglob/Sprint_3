import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators

class TestConstructor:


    def test_constructor_section_transitions_sauсe(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')


        driver.find_element(*TestLocators.SAUCE_BTN).click()
        assert driver.find_element(*TestLocators.SAUCE_BTN).get_attribute('class') == TestLocators.selector
        driver.quit()

    def test_constructor_section_transitions_topping(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')

        driver.find_element(*TestLocators.TOPPING_BTN).click()
        assert driver.find_element(*TestLocators.TOPPING_BTN).get_attribute('class') == TestLocators.selector
        driver.quit()


    def test_constructor_section_transitions_brides(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.TOPPING_BTN).click()
        driver.find_element(*TestLocators.BRIDES_BTN).click()
        assert driver.find_element(*TestLocators.BRIDES_BTN).get_attribute('class') == TestLocators.selector
        driver.quit()

