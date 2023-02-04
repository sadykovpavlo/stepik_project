from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_text_empty_basket(self):
        """I expect text Your basket empty is present"""
        text_empty_basket = self.wait_visibility_of_element(*BasketPageLocators.EMPTY_TEXT)
        text_empty_basket_text = text_empty_basket.text
        assert text_empty_basket_text == 'Your basket is empty. Continue shopping', 'Basket not empty'

    def should_not_be_checkout_button(self):
        """If basket is empty I expect checkout button is not present"""
        no_checkout_button = self.is_not_element_present(*BasketPageLocators.CHECKOUT_BUTTON)
        assert no_checkout_button, "Checkout button present"

    def should_not_be_item(self):
        """If basket is empty no href is present"""
        no_item = self.is_not_element_present(*BasketPageLocators.ITEM_HREF)
        assert no_item, 'Item present'
