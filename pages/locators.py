from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, ".col-sm-6.login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".col-sm-6.register_form")
    EMAIL_WINDOW = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD1_WINDOW = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD2_WINDOW = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BTN = (By.CSS_SELECTOR, "[name=registration_submit]")


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CSS_SELECTOR, ".btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main>h1")
    PRODUCT_NAME_IN_ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-success.fade.in>.alertinner>strong")
    PRODUCT_COST = (By.CSS_SELECTOR, ".price_color")
    PRODUCT_COST_IN_BASKET_COST_MESSAGE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert.alert-safe.alert-noicon.alert-success.fade.in>.alertinner")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link")
    BASKET_BTN = (By.CSS_SELECTOR, "span>a.btn.btn-default")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "#content_inner>div")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")