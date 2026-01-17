import os

import allure
import allure_commons
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selene import browser, support

from settings import settings
from utils.attach import attach_bstack_video


@pytest.fixture(scope='function', autouse=True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({
        # 'platformName': 'Android',
        'platformVersion': '11.0',
        'deviceName': 'Google Pixel 5',
        'app': 'bs://sample.app',

        'bstack:options': {
            'projectName': 'Py project BStack',
            'buildName': 'browserstack-build',
            'sessionName': 'BStack first_test',

            'userName': settings.bstack_userName,
            'accessKey': settings.bstack_accessKey,
        }
    })

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            'https://hub.browserstack.com/wd/hub',
            options=options
        )
    # browser.config.driver = options
    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    browser.config._wait_decorator = support._logging.wait_with(
        context=allure_commons._allure.StepContext
    )

    yield

    allure.attach(
        browser.driver.get_screenshot_as_png(),
        name='screenshot',
        attachment_type=allure.attachment_type.PNG
    )

    allure.attach(
        browser.driver.page_source,
        name='screen xml dump',
        attachment_type=allure.attachment_type.XML
    )

    session_id = browser.driver.session_id

    with allure.step('tear down app session'):
        browser.quit()

    attach_bstack_video(session_id)
