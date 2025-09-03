from playwright.sync_api import Page, expect
from tools.logger.logger import get_logger
import allure
logger = get_logger("BASE_ELEMENT")


class BaseElements:
    def __init__(self, page: Page, name: str):
        self.page = page
        self.name = name

    @property
    def type_of(self):
        return "base element"

    def get_locator(self, test_id: str, sub_attribute: str):
        return self.page.locator(f'//*[@id="{test_id}"]{sub_attribute}')

    def to_be_visible(self):
        step=f"Expect {self.type_of}: '{self.name}' to be visible"
        with allure.step(step):
            locator=self.get_locator()
            logger.info(step)
            expect(locator).to_be_visible()