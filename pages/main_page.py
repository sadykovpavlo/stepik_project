from .base_page import BasePage
from .locators import MainPageLocator


class MainPage(BasePage):

    def go_to_login_page(self):
        login_button = self.browser.find_element(*MainPageLocator.LOGIN_LINK)
        login_button.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocator.LOGIN_LINK), 'Login link not present'
