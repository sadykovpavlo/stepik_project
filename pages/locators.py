from selenium.webdriver.common.by import By


class MainPageLocator:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocator:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')

    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocator:
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form button')

    PRODUCT = (By.CSS_SELECTOR, 'div h1')

    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div .price_color:nth-child(2)')

    BASKET_FIELD = (By.CSS_SELECTOR, '.col-sm-3.price_color')

    PRICE_POPUP = (By.CSS_SELECTOR, '.alertinner p strong')

    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, 'span .btn-default:nth-child(1)')


