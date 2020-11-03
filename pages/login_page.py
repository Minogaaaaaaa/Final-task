from .base_page import BasePage
from pages.locators import LoginPageLocators
import time



class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "url dont't have 'login'"
        assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        assert True

    def register_new_user(self):
        
        email_window = self.browser.find_element(*LoginPageLocators.EMAIL_WINDOW)
        password1_window = self.browser.find_element(*LoginPageLocators.PASSWORD1_WINDOW)
        password2_window = self.browser.find_element(*LoginPageLocators.PASSWORD2_WINDOW)
        email_window.send_keys(str(time.time()) + "@fakemail.org")
        password1_window.send_keys("01536test7")
        password2_window.send_keys("01536test7")
        button = self.browser.find_element(*LoginPageLocators.REGISTRATION_BTN)
        button.click()

