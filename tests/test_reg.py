import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators

class TestRegSuccess:

    def test_registration_no_empty_name(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//fieldset[1]/div/div/input')
        ))
        driver.find_element(*TestLocators.INPUT_NAME_REG_PAGE).send_keys('ВАСЯ')
        assert len(driver.find_element(*TestLocators.INPUT_NAME_REG_PAGE).get_attribute('value')) > 0

    def test_registration_valid_e_mail(self, make_login, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//fieldset[2]/div/div/input')
        ))
        driver.find_element(*TestLocators.INPUT_EMAIL_REG_PAGE).send_keys(make_login)
        d = driver.find_element(*TestLocators.INPUT_EMAIL_REG_PAGE).get_attribute('value')
        assert d.count('@') == 1 and d[0] != '@' and d.count('.') > 0 and d.rfind('.') > d.find('@')

    def test_registration_valid_password(self, make_password, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//fieldset[3]/div/div/input')
        ))
        driver.find_element(*TestLocators.INPUT_PASSWORD_REG_PAGE).send_keys(make_password)
        c = driver.find_element(*TestLocators.INPUT_PASSWORD_REG_PAGE).get_attribute('value')
        assert len(c) >= 6

    def test_registration_invalid_password(self, driver):
        driver.get('https://stellarburgers.nomoreparties.site/register')
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(
            (By.XPATH, '//fieldset[3]/div/div/input')
        ))
        driver.find_element(*TestLocators.INPUT_PASSWORD_REG_PAGE).send_keys('12345')
        driver.find_element(*TestLocators.SIGN_IN_BTN_LOGIN_PAGE).click()

        assert driver.find_element(*TestLocators.PASSWORD_ERROR).text == 'Некорректный пароль'



