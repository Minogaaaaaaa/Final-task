from .base_page import BasePage
from.locators import BasePageLocators

class BasketPage(BasePage):

    def should_be_product_in_basket(self):
        assert self.is_element_present(*BasePageLocators.PRODUCT_IN_BASKET), \
            "Basket is empty, but should not be"


    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasePageLocators.PRODUCT_IN_BASKET), \
            "Basket is not empty, but should be"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_MESSAGE), \
            "Have not message 'Basket is empty', but should be"

    def should_not_be_empty_basket_message(self):
        assert self.is_not_element_present(*BasePageLocators.EMPTY_BASKET_MESSAGE), \
            "Have message 'Basket is empty', but should not be"