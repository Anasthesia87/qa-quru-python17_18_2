import allure
import allure_commons
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser, support
from dotenv import load_dotenv
import os
import config
from selene.support.shared import config

from utils import attach


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


login = os.getenv('BROWSERSTACK_LOGIN')
access_key = os.getenv('BROWSERSTACK_ACCESS_KEY')
project = os.getenv('BROWSERSTACK_PROJECT')
timeout = os.getenv('BROWSERSTACK_TIMEOUT')
app = os.getenv('BROWSERSTACK_APP')


def android_management():
    options = UiAutomator2Options().load_capabilities({
        'platformName': 'android',
        'deviceName': 'Samsung Galaxy S22 Ultra',
        'platformVersion': '12.0',
        'app': app,
        'bstack:options': {
            'sessionName': 'bstack_first_test',
            'projectName': project,
            'buildName': 'browserstack-build-1',
            "userName": login,
            "accessKey": access_key
        }
    })
    return options


def ios_management():
    options = XCUITestOptions().load_capabilities({
        'platformName': 'ios',
        'deviceName': 'iPhone 12 Pro Max',
        'platformVersion': '16',
        'app': app,
        'bstack:options': {
            'sessionName': 'bstack_first_test',
            'projectName': project,
            'buildName': 'browserstack-build-1',
            "userName": login,
            "accessKey": access_key
        }
    })
    return options


def pytest_addoption(parser):
    parser.addoption(
        '--platform',
        default='android'
    )


@pytest.fixture(scope='function', autouse=True)
def mobile_settings(request):
    platform = request.config.getoption('--platform')
    if platform == 'android':
        options = android_management()
    elif platform == 'ios':
        options = ios_management()
    else:
        return

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            'http://hub.browserstack.com/wd/hub',
            options=options,
        )
    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield platform

    attach.add_screenshot(browser)

    attach.add_xml(browser)

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    attach.add_video(config.session_id, config.login, config.access_key)
