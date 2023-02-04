import math
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.timeout = timeout
        self.EC = EC
        self.Wait = WebDriverWait

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        else:
            return True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def wait_visibility_of_element(self, how, what):
        element = self.Wait(self.browser, self.timeout).until(self.EC.visibility_of_element_located(locator=(how, what)))
        return element

    def wait_visibility_of_elements(self, how, what):
        self.Wait(self.browser, self.timeout).until(self.EC.visibility_of_all_elements_located(locator=(how, what)))

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self):
        basket_button = self.browser.find_element(*BasePageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_busked_page(self):
        basked_h1 = self.wait_visibility_of_element(*BasePageLocators.BASKET_H1)
        assert basked_h1.text == 'Basket', 'No h1 element on basket page'

    def should_be_account_icon(self):
        account_icon = self.wait_visibility_of_element(*BasePageLocators.ACCOUNT_ICON)
        assert account_icon, 'User not register'

