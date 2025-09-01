import pytest
from playwright.sync_api import Page
from pages.index_page.index_page import IndexPage


@pytest.fixture
def index_page(browser_page:Page)->IndexPage:
    return IndexPage(page=browser_page)