
from playwright.sync_api import Page
from tools.logger import get_logger
import allure

logger = get_logger("BASE_PAGE")


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def visit(self, url: str):
        step = f"Opening the {url}"
        with allure.step(step):
            logger.info(step)
            return self.page.goto(url=url, wait_until="domcontentloaded")

    def reload(self):
        step = f"Reloading the page"
        with allure.step(step):
            logger.info(step)
            return self.page.reload(wait_until="domcontentloaded")
