from _pytest.fixtures import SubRequest
from allure_commons.types import AttachmentType
from playwright.sync_api import Playwright
import pytest
import allure
from config import settings
from tools.mock import mock


@pytest.fixture(params=settings.http_data.browsers)
def browsers_page(playwright: Playwright, request: SubRequest):
    browsers_name = request.param
    browser = playwright[browsers_name].launch(headless=settings.http_data.headless)
    context = browser.new_context(record_video_dir=settings.record_video_dir)
    context.tracing.start(screenshots=True, sources=True, snapshots=True)
    page = context.new_page()
    mock(page)
    yield page

    path = f"{settings.tracing}/{request.node.name}.zip"
    context.tracing.stop(path=path)
    allure.attach.file(source=page.video.path(), name="video", attachment_type=AttachmentType.WEBM)
    allure.attach.file(source=path, name="tracing", extension="zip")
