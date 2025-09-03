import pytest
from _pytest.fixtures import SubRequest
from allure_commons.types import AttachmentType
from playwright.sync_api import Playwright, Page
import allure

from config import settings

from tools.mock_static_recourses.mock_static_recourses import mock_static_recourses


@pytest.fixture(params=settings.http_data.browsers)
def browser_page(playwright: Playwright, request: SubRequest) -> Page:
    browser_name = request.param
    browser = getattr(playwright,browser_name).launch(headless=settings.http_data.headless)

    context = browser.new_context(record_video_dir=settings.record_video_dir)
    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    page = context.new_page()
    mock_static_recourses(page)
    yield page

    path_tracing = f'{settings.tracing_dir}/{request.node.name}.zip'
    context.tracing.stop(path=path_tracing)
    allure.attach.file(source=path_tracing, name="tracing", extension="zip")
    allure.attach.file(source=page.video.path(), name="video", attachment_type=AttachmentType.WEBM)
