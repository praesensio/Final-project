from pages.main_page import MainPage
from pages.login_page import LoginPage
import pytest

@pytest.mark.need_review_custom_scenarios
def test_guest_can_registrated(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)    
    page.open()                      
    page.go_to_login_page()
    page = LoginPage(browser, link)    
    page.should_be_login_url()
    page.should_be_register_form()

@pytest.mark.need_review_custom_scenarios
def test_guest_can_log_in(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)    
    page.open()                      
    page.go_to_login_page()
    page = LoginPage(browser, link)    
    page.should_be_login_url()
    page.should_be_login_form()
