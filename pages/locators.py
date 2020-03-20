from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REG_EMAIL = (By.NAME, "registration-email")
    REG_PASS1 = (By.NAME, "registration-password1")
    REG_PASS2 = (By.NAME, "registration-password2")
    LOGIN = (By.NAME, "login-username")
    PASSWORD = (By.NAME, "login-password")
    LOGIN_BUTTON = (By.NAME, "login_submit")
    REG_BUTTON = (By.NAME, "registration_submit")


class ProductPageLocators():
    ADD_IN_BASKET = (By.XPATH, '//button[contains(text(),"Добавить в корзину")]')
    SHOW_BASKET = (By.XPATH, '//a[contains(text(),"Посмотреть корзину")]')
    SUCCESS_MESSAGE_AFTER_ADD_IN_BASKET = (By.CSS_SELECTOR, '.alert-safe:nth-child(1) .alertinner> strong')

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    BASKET_LINK = (By.CSS_SELECTOR, '.btn-group > a.btn-default')
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, '#content_inner > p')
    BASKET_GOODS = (By.CSS_SELECTOR, "basket-items")
