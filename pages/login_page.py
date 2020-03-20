from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self, browser):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "Wrong page"


    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN), "Login for log in is not presented"
        assert self.is_element_present(*LoginPageLocators.PASSWORD), "Password for log in registration is not presented"


    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), "Email for registration is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS1), "Password1 for registration is not presented"
        assert self.is_element_present(*LoginPageLocators.REG_PASS2), "Password2 for registration is not presented"


    def register_new_user(self):
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time()) + "@fakemail.org"
        email_field = self.browser.find_element(*LoginPageLocators.REG_EMAIL).send_keys(email)
        password_field1 = self.browser.find_element(*LoginPageLocators.REG_PASS1).send_keys(password)
        password_field2 = self.browser.find_element(*LoginPageLocators.REG_PASS2).send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REG_BUTTON).click()
    
