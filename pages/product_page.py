from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators
from .locators import BasketPageLocators


class ProductPage(BasePage):
    def should_be_promo_url(self):
        assert '?promo=newYear' in self.browser.current_url, "Wrong page"

    def add_good(self):
        assert self.is_element_present(*ProductPageLocators.ADD_IN_BASKET), "No button to add a new good"
        button = self.browser.find_element(*ProductPageLocators.ADD_IN_BASKET)
        button.click()
    def really_in_basket(self):
        gotcha = self.browser.find_element_by_css_selector('.product_main > h1')
        basket = gotcha.text
        alert1 = self.browser.find_element_by_xpath('(.//*[@class="alertinner "]//strong)[1]')
        message1 = alert1.text
        assert basket in message1
        gotcha2 = self.browser.find_element_by_xpath('(.//*[@class="price_color"])[1]')
        basket2 = gotcha2.text
        alert2 = self.browser.find_element_by_xpath('(.//*[@class="alertinner "]//strong)[3]')
        message2 = alert2.text
        assert basket2 in message2

    def go_to_basket_page(self):
        link = self.browser.find_element(*BasketPageLocators.BASKET_LINK)
        link.click()

        
    def should_not_be_success_message_after_adding_good(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_AFTER_ADD_IN_BASKET), "Success message shoul not be presented"


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE_AFTER_ADD_IN_BASKET), "Success message should not be presented"      
        
        
    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE_AFTER_ADD_IN_BASKET), "Success message should be disappeared"         
        

