from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import ProductPageLocators
from pages.locators import BasketPageLocators
import pytest
import time

@pytest.mark.need_review_custom_scenarios
@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                pytest.param(
                                      "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo"
                                      "=offer7", marks=pytest.mark.xfail)])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"{link}"
    page = ProductPage(browser, link)    
    page.open()
    page.add_good()
    page.solve_quiz_and_get_code()
    page.really_in_basket()


@pytest.mark.xfail(reason="Success message should be presented")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()  
    page.add_good()  
    page.should_not_be_success_message_after_adding_good()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message_after_adding_good()

@pytest.mark.xfail(reason="Success message is disappeared")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open() 
    page.add_good()  
    page.success_message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()            
    page.go_to_basket_page()
    page = BasketPage(browser, link)
    page.should_be_empty_basket()

class TestUserAddToBasketFromProductPage(BasePage):
    def test_user_cant_see_success_message(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message_after_adding_good()
    

    @pytest.mark.need_review_custom_scenarios
    @pytest.mark.need_review
    @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                    pytest.param(
                                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo"
                                          "=offer7", marks=pytest.mark.xfail)])
    def test_user_can_add_product_to_basket(browser, link):
        link = f"{link}"
        page = ProductPage(browser, link)    
        page.open()
        page.add_good()
        page.solve_quiz_and_get_code()
        page.really_in_basket()


    @pytest.mark.need_review_custom_scenarios
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user()
        browser.implicitly_wait(5)
        page.should_be_authorized_user() 
