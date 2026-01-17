from appium.webdriver.common.appiumby import AppiumBy

SEARCH_OPEN = (AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")
SEARCH_INPUT = (AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")
RESULT_TITLE = (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")
RESULT_CONTAINER = (AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_container")