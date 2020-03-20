from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):
    


    def should_be_empty_basket(self):
        basket_message = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY)
        assert basket_message.is_displayed(), "empty basket message is not presented"

    def should_be_good_in_basket(self):
        product_in_basket = self.browser.find_element(*BasketPageLocators.BASKET_GOOD)
        assert product_in_basket.is_displayed(), "product in basket is not presented"

    def should_not_be_good_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_GOOD), \
            "Product in basket is presented, but should not be"
