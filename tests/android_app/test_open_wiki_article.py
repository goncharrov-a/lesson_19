import allure
import pytest
from selene import browser, have

from tests.android_app.locators.wiki_search import (
    SEARCH_OPEN,
    SEARCH_INPUT,
    RESULT_TITLE,
    RESULT_CONTAINER,
)


@allure.feature("Поиск")
@allure.story("Открытие статьи")
@allure.title("Открыть первую статью из результатов поиска")
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
@allure.title("Поиск: результаты содержат запрос")
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
