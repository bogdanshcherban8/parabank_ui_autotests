from playwright.sync_api import Page, expect
from tools.logger.logger import get_logger
import allure

logger = get_logger("BASE_ELEMENT")


class BaseElement:
    def __init__(self, page: Page, test_id: str, sub_attribute:str, name: str):
        self.page = page
        self.name = name
        self.test_id=test_id
        self.sub_attribute=sub_attribute
    @property
    def type_of(self):
        return "base element"

    def get_locator(self):
        return self.page.locator(f'//*[@id="{self.test_id}"]{self.sub_attribute}')

    def to_be_visible(self):
        step = f"Expect {self.type_of}: '{self.name}' to be visible"
        with allure.step(step):
            locator = self.get_locator()
            logger.info(step)
            expect(locator).to_be_visible()
