import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from urls import Urls

class TestPersonalAccount:

    def test_go_to_personal_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.ACC_BTN_START_PAGE).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()


    def test_from_personal_account_to_constructor(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(*TestLocators.CONST_BTN).click()
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()


    def test_from_personal_to_logo(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(*TestLocators.LOGO_BTN).click()

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        driver.quit()


    def test_out_from_personal_account(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/login')
        driver.find_element(*TestLocators.MAIL_INPUT).send_keys(*Urls.mail)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(*Urls.password)
        driver.find_element(*TestLocators.SIGN_IN_BTN_LOGIN_PAGE).click()
        driver.find_element(*TestLocators.ACC_BTN_START_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//ul/li[3]/button')
        ))
        driver.find_element(*TestLocators.OUT_BTN).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//form/button')
        ))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
        driver.quit()
