import allure
import pytest
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have

SEARCH_OPEN = (AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")
SEARCH_INPUT = (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")
RESULT_TITLE = (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")
RESULT_CONTAINER = (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_container")


@allure.feature("Поиск")
@allure.story("Открытие статьи")
@allure.title("Открыть первую статью из результатов поиска по запросу")
@pytest.mark.android
def test_open_article_from_search():
    query = "Selene"

    with allure.step("Открыть поиск"):
        browser.element(SEARCH_OPEN).click()

    with allure.step(f"Ввести запрос: {query}"):
        browser.element(SEARCH_INPUT).type(query)

    with allure.step("Проверить, что есть результаты"):
        results = browser.all(RESULT_TITLE)
        results.should(have.size_greater_than(0))

    with allure.step("Открыть первый результат"):
        browser.element(RESULT_CONTAINER).click()


@allure.feature("Поиск")
@allure.story("Поиск статьи")
@allure.title("Поиск: результаты содержат введённый запрос")
@pytest.mark.android
def test_search():
    query = "Appium"

    with allure.step("Открыть поиск"):
        browser.element(SEARCH_OPEN).click()

    with allure.step(f"Ввести запрос: {query}"):
        browser.element(SEARCH_INPUT).type(query)

    with allure.step("Проверить, что найден хотя бы один результат"):
        results = browser.all(RESULT_TITLE)
        results.should(have.size_greater_than(0))

    with allure.step(f"Проверить, что первый результат содержит: {query}"):
        results.first.should(have.text(query))
