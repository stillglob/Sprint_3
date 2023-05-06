import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from urls import Urls

class TestSignIn:

    def test_sign_in_from_start_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.SIGN_IN_ACC_BTN_START_PAGE).click()
        driver.find_element(*TestLocators.MAIL_INPUT).send_keys(*Urls.mail)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(*Urls.password)
        driver.find_element(*TestLocators.SIGN_IN_BTN_LOGIN_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.SIGN_IN_ACC_BTN_START_PAGE
        ))
        assert 'Оформить заказ' == driver.find_element(*TestLocators.SIGN_IN_ACC_BTN_START_PAGE).text
        driver.quit()

    def test_sign_in_from_personal_area(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site')
        driver.find_element(*TestLocators.ACC_BTN_START_PAGE).click()
        driver.find_element(*TestLocators.MAIL_INPUT).send_keys(*Urls.mail)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(*Urls.password)
        driver.find_element(*TestLocators.SIGN_IN_BTN_LOGIN_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            TestLocators.SIGN_IN_ACC_BTN_START_PAGE
        ))
        assert 'Оформить заказ' == driver.find_element(*TestLocators.SIGN_IN_ACC_BTN_START_PAGE).text

        driver.quit()

    def test_sign_in_from_registration_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        driver.execute_script("window.scrollTo(0, 250);")
        driver.find_element(*TestLocators.SIGN_IN_BTN_FROM_REG_FORGOT_PAGE).click()
        driver.find_element(*TestLocators.MAIL_INPUT).send_keys(*Urls.mail)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(*Urls.password)
        driver.find_element(*TestLocators.SIGN_IN_BTN_LOGIN_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.SIGN_IN_ACC_BTN_START_PAGE
        ))

        assert 'Оформить заказ' == driver.find_element(*TestLocators.SIGN_IN_ACC_BTN_START_PAGE).text
        driver.quit()

    def test_sign_in_from_forgot_page(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/forgot-password')
        driver.execute_script("window.scrollTo(0, 250);")
        driver.find_element(*TestLocators.SIGN_IN_BTN_FROM_REG_FORGOT_PAGE).click()
        driver.find_element(*TestLocators.MAIL_INPUT).send_keys(*Urls.mail)
        driver.find_element(*TestLocators.PASSWORD_INPUT).send_keys(*Urls.password)
        driver.find_element(*TestLocators.SIGN_IN_BTN_LOGIN_PAGE).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(
            TestLocators.SIGN_IN_ACC_BTN_START_PAGE
        ))
        assert 'Оформить заказ' == driver.find_element(*TestLocators.SIGN_IN_ACC_BTN_START_PAGE).text
        driver.quit()

