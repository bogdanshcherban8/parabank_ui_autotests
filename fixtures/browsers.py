from playwright.sync_api import Playwright, Page
from config import settings
import pytest
@pytest.fixture(params=settings.http_data.browsers)
def browser_page(playwright: Playwright, request) -> Page:
    browsers = request.param
    browser = getattr(playwright, browsers).launch(headless=settings.http_data.headless)
    context = browser.new_context()
    context.tracing.start(snapshots=True, screenshots=True, sources=True)
    page = context.new_page()
    yield page
    context.tracing.stop(path=settings.path_data.trace + ".zip")
    context.close()
    browser.close()


