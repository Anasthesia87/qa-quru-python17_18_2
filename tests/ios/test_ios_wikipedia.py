import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
import allure


def test_ios_text_input(mobile_settings):
    if mobile_settings == 'android':
        pytest.skip('Not supported on Android')
    with allure.step('Input text'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Button')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Input")).send_keys('Pumpkin Eater\n')
    with allure.step('Verify added text'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Text Output")).should(have.text('Pumpkin Eater'))


