from re import Pattern

from playwright.sync_api import Page, expect
import allure
from tools.logger import get_logger
from faker import Faker

logger = get_logger("BASE_COMPONENT")


class BaseComponent:
    def __init__(self, page: Page):
        self.page = page
        self.fake = Faker()


    def check_current_url(self, expected_url: Pattern[str]):
        step = f"Checking that current url matches with {expected_url.pattern}"
        with allure.step(step):
            logger.info(step)
            return expect(self.page).to_have_url(expected_url.pattern)
