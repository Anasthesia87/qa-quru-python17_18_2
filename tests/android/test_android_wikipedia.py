import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have
import allure


def test_android_wiki_search(mobile_settings):
    if mobile_settings == 'ios':
        pytest.skip('Not supported on IOS')
    with allure.step('Find the search field and type the search query'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('BrowserStack')

    with allure.step('Verify found content'):
        search_results = browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"))
        search_results.should(have.size_greater_than(0))
        search_results.first.should(have.text('BrowserStack'))


def test_android_wiki_search_article_by_title_python(mobile_settings):
    if mobile_settings == 'ios':
        pytest.skip('Not supported on IOS')
    with allure.step('Find the search field and type the search query'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Python')

    with allure.step('Verify found content'):
        search_results = browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title"))
        search_results.first.should(have.text('Python'))

    with allure.step('Open first founded page'):
        search_results.first.click()
