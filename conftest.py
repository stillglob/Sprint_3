import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import random as r

@pytest.fixture
def make_login():
    login_bank = ('abcdefghijklnopqrstuvwxyz1234567890')
    login = ''
    for n in range(10):
        login += r.choice(login_bank)
    return login + '@ya.ru'

@pytest.fixture
def make_password():
    pass_bank = ('+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyz1234567890')
    password = ''
    for c in range(16):
        password += r.choice(list(pass_bank))
    return password

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    return driver

