from .base_page import BasePage
from.locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):

    def add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()


    def should_be_add_to_basket_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        print(product_name)
        product_name_in_add_to_basket_message = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_ADD_TO_BASKET_MESSAGE).text
        print(product_name_in_add_to_basket_message)
        assert product_name == product_name_in_add_to_basket_message, "product name in message is different"
        assert True

    def should_be_basket_cost_message(self):
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        product_cost_in_basket_cost_message = self.browser.find_element(*ProductPageLocators.PRODUCT_COST_IN_BASKET_COST_MESSAGE).text 
        print(product_cost)
        print(product_cost_in_basket_cost_message)
        assert product_cost in product_cost_in_basket_cost_message, "basket cost in message is different"
        assert True
