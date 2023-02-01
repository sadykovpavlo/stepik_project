from .base_page import BasePage
from .locators import LoginPageLocator


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):

        login_url = self.browser.current_url
        assert 'login' in login_url, 'login url not present'

    def should_be_login_form(self):

        login_form = self.is_element_present(*LoginPageLocator.LOGIN_FORM)
        assert login_form, 'Login form is not present'

    def should_be_register_form(self):

        register_form = self.is_element_present(*LoginPageLocator.REGISTER_FORM)
        assert register_form, 'Register form not present'
