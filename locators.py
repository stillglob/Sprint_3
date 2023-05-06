from selenium.webdriver.common.by import By

class TestLocators:
    SIGN_IN_ACC_BTN_START_PAGE = By.XPATH, '//section[2]/div/button'
    MAIL_INPUT = By.XPATH, '//form/fieldset[1]//input'
    PASSWORD_INPUT = By.XPATH, '//form/fieldset[2]//input'
    SIGN_IN_BTN_LOGIN_PAGE = By.XPATH, '//form/button'
    ACC_BTN_START_PAGE = By.XPATH, '//div/header/nav/a/p'
    SIGN_IN_BTN_FROM_REG_FORGOT_PAGE = By.XPATH, '//div/p/a'
    INPUT_NAME_REG_PAGE = By.XPATH, '//fieldset[1]/div/div/input'
    INPUT_EMAIL_REG_PAGE = By.XPATH, '//fieldset[2]/div/div/input'
    INPUT_PASSWORD_REG_PAGE = By.XPATH, '//fieldset[3]/div/div/input'
    PASSWORD_ERROR = By.XPATH, '//fieldset[3]/div/p'
    SAUCE_BTN = By.XPATH, "//section[1]/div[1]/div[2]"
    TOPPING_BTN = By.XPATH, "//section[1]/div[1]/div[3]"
    BRIDES_BTN = By.XPATH, "//section[1]/div[1]/div[1]"
    selector_class_const = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
    CONST_BTN = By.XPATH, '//ul/li[1]/a'
    LOGO_BTN = By.XPATH, '//header/nav/div'
    OUT_BTN = By.XPATH, '//ul/li[3]/button'
    selector = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect'
