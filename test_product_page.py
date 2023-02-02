import pytest

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage


@pytest.mark.parametrize('link_test',
                         {"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                          "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"})
@pytest.mark.skip
def test_guest_can_add_product_to_basket(browser, link_test):
    link = f"{link_test}"
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.should_be_product()

    product_page.should_be_price()

    product_page.should_be_basket_button()

    product_page.should_be_add_button()

    product_page.add_product_to_busked()

    product_page.solve_quiz_and_get_code()

    product_page.should_be_equals_name()

    product_page.should_be_equals_price()


@pytest.mark.xfail(reason='Fail is expected')
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.add_product_to_busked()

    product_page.should_not_be_element()


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_element()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/'
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.add_product_to_busked()

    product_page.should_disappeared_element()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    product_page = ProductPage(browser, link)

    product_page.open()

    product_page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)

    login_page.should_be_login_page()

    login_page.should_be_login_form()

    login_page.should_be_login_url()
