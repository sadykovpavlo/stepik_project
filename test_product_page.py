from .pages.product_page import ProductPage


def test_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    product_page = ProductPage(browser, link)
    product_page.open()

    product_page.should_be_product()

    product_page.should_be_price()

    product_page.should_be_basket_button()

    product_page.should_be_add_button()

    product_page.add_product_to_busked()

    product_page.solve_quiz_and_get_code()
