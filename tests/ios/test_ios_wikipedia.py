import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
import allure


def test_ios_wiki_search(mobile_settings):
    if mobile_settings == 'android':
        pytest.skip('Not supported on Android')
    with allure.step('Find the search field and type the search query'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Button')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Input')).send_keys('Java')
    with allure.step('Verify found content'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Output')).should(have.text('Java'))
