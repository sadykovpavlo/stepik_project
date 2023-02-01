from .base_page import BasePage
from .locators import ProductPageLocator


class ProductPage(BasePage):
    def product_page(self):
        self.should_be_product()
        self.should_be_price()
        self.should_be_add_button()
        self.should_be_basket_button()
        self.should_be_equals_price()

    def should_be_product(self):
        """Check if product present on page"""
        product = self.is_element_present(*ProductPageLocator.PRODUCT)
        assert product, 'No product on the page'

    def should_be_price(self):
        """Check if price of product present"""
        price_product = self.is_element_present(*ProductPageLocator.PRODUCT_PRICE)
        assert price_product, "No price on the page"

    def should_be_basket_button(self):
        """Check if redirect to basket button is present"""
        basket_button = self.is_element_present(*ProductPageLocator.VIEW_BASKET_BUTTON)
        assert basket_button, 'No basket button'

    def should_be_add_button(self):
        """Check if add product to basket button is present"""
        button = self.is_element_present(*ProductPageLocator.SUBMIT_BUTTON)
        assert button, 'No basket button'

    def add_product_to_busked(self):
        """Method to add product to basket"""
        button = self.browser.find_element(*ProductPageLocator.SUBMIT_BUTTON)
        button.click()

    def should_be_equals_price(self):
        """Not ready but in progress"""
        price_in_popup = self.wait_visibility_of_element(*ProductPageLocator.PRICE_POPUP)
        product_price = self.browser.find_element(*ProductPageLocator.PRODUCT_PRICE)
        assert price_in_popup in product_price, 'Price not equals'
