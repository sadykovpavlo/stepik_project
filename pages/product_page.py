from .base_page import BasePage
from .locators import ProductPageLocator
import time


class ProductPage(BasePage):
    def product_page(self):
        self.should_be_product()
        self.should_be_price()
        self.should_be_add_button()
        self.should_be_basket_button()
        self.should_be_equals_name()
        self.get_name_of_element_in_popup()
        self.get_name_of_product()
        self.get_price_in_popup()
        self.get_price_of_product()

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

    def get_name_of_element_in_popup(self):
        """method to get a price in popup"""
        name_in_popup = self.wait_visibility_of_element(*ProductPageLocator.NAME_IN_POPUP)
        return name_in_popup.text

    def get_name_of_product(self):
        """method ti get name of product on the page"""
        product_name = self.browser.find_element(*ProductPageLocator.PRODUCT)
        return product_name.text

    def should_be_equals_name(self):
        """assert method"""
        name_in_popup = self.get_name_of_element_in_popup()
        name_of_product = self.get_name_of_product()
        assert name_of_product == name_in_popup

    def get_price_in_popup(self):
        price_in_popup = self.browser.find_element(*ProductPageLocator.PRICE_IN_POPUP)
        return price_in_popup.text

    def get_price_of_product(self):
        price_of_product = self.browser.find_element(*ProductPageLocator.PRODUCT_PRICE)
        return price_of_product.text

    def should_be_equals_price(self):
        price_in_popup = self.get_price_in_popup()
        price_of_product = self.get_price_of_product()
        assert price_of_product == price_in_popup, 'Price not equals'

    def should_not_be_element(self):
        element = self.is_not_element_present(*ProductPageLocator.POPUP)
        assert element, 'Element present on the page'

    def should_disappeared_element(self):
        element = self.is_disappeared(*ProductPageLocator.POPUP)
        assert element, 'Element still present on the page'


