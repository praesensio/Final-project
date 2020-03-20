from pages.main_page import MainPage
from pages.base_page import BasePage
from selenium.common.exceptions import NoSuchElementException
from pages.locators import MainPageLocators
from pages.login_page import LoginPage
from pages.locators import BasketPageLocators
from pages.basket_page import BasketPage
import time
import pytest



@pytest.mark.login_guest
class TestLoginFromMainPage():

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)    
        page.open()                      
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page(browser)

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

def test_guest_can_registrated(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)    
    page.open()                      
    page.should_be_login_url()
    page.should_be_register_form()

@pytest.mark.need_review_custom_scenarios
def test_guest_can_log_in(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser, link)    
    page.open()                      
    page.should_be_login_url()
    page.should_be_login_form()

    
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)    
    page.open()            
    page.go_to_basket_page()
    page = BasketPage(browser, link)
    page.should_be_empty_basket()



    
    

