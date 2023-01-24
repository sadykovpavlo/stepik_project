import pytest
from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome', help='Write browser name')
    parser.addoption('--language', action='store', default='en-gb', help='Set language')


@pytest.fixture(scope='function')
def browser(request):
    browser_name = request.config.getoption('browser_name')
    browser_language = request.config.getoption('language')
    browser = None
    if browser_name == 'chrome':
        option = Options()
        option.add_experimental_option('prefs', {'intl.accegipt_languages': f'{browser_language}'})
        browser = Chrome(options=option)
    elif browser_name == 'firefox':
        browser = Firefox()
    yield browser
    browser.quit()
