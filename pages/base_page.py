from playwright.sync_api import Page
import allure
from tools.logger import get_logger

logger = get_logger("BASE_PAGE")


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        step = f"Open {url}"
        with allure.step(step):
            logger.info(step)
            self.page.goto(url=url, wait_until="domcontentloaded")
