from ..functions.random_string_generator import random_string
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
        login_form = self.wait_visibility_of_element(*LoginPageLocator.LOGIN_FORM)
        assert login_form, 'Login form is not present'

    def should_be_register_form(self):
        register_form = self.is_element_present(*LoginPageLocator.REGISTER_FORM)
        assert register_form, 'Register form not present'

    def register_new_user(self):
        password = random_string()
        email_text = random_string()
        password_field = self.browser.find_element(*LoginPageLocator.REGISTRATION_PASSWORD_FIELD)
        password_field.send_keys(password)
        confirm_pass = self.browser.find_element(*LoginPageLocator.CONFIRM_PASS_FIELD)
        confirm_pass.send_keys(password)
        email_field = self.browser.find_element(*LoginPageLocator.REGISTRATION_EMAIL_FIELD)
        email_field.send_keys(f'{email_text.lower()}@fakemail.com')
        register_button = self.browser.find_element(*LoginPageLocator.REGISTER_BUTTON)
        register_button.click()
