from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.CSS_SELECTOR, '.basket-mini .btn:nth-child(1)')
    BASKET_H1 = (By.CSS_SELECTOR, 'div h1')
    ACCOUNT_ICON = (By.CSS_SELECTOR, 'i[class="icon-user"]')


class BasketPageLocators:
    EMPTY_TEXT = (By.CSS_SELECTOR, '#content_inner p')
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, "div[class='row'] a.btn-lg")
    ITEM_HREF = (By.CSS_SELECTOR, 'div h3 a')


class MainPageLocator:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocator:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    REGISTRATION_EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='registration-email']")
    REGISTRATION_PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='registration-password1']")
    CONFIRM_PASS_FIELD = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocator:
    SUBMIT_BUTTON = (By.CSS_SELECTOR, '#add_to_basket_form button')
    PRODUCT = (By.CSS_SELECTOR, 'div h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div .price_color:nth-child(2)')
    BASKET_FIELD = (By.CSS_SELECTOR, '.col-sm-3.price_color')
    NAME_IN_POPUP = (By.CSS_SELECTOR, '.alert:nth-child(1) .alertinner > strong')
    VIEW_BASKET_BUTTON = (By.CSS_SELECTOR, 'span .btn-default:nth-child(1)')
    PRICE_IN_POPUP = (By.CSS_SELECTOR, '.alertinner p strong')
    POPUP = (By.CSS_SELECTOR, '#messages div:nth-child(1)')




