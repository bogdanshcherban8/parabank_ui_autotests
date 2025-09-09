import allure
from playwright.sync_api import expect

from tools.logger import get_logger

logger = get_logger("BASE_ELEMENT")
class BaseElement:
    def __init__(self, page, test_id: str, attribute: str, name: str):
        self.page = page
        self.test_id = test_id
        self.attribute = attribute
        self.name = name

    @property
    def type_of(self):
        return "base element"

    def get_locator(self):
        return self.page.locator(f'//*[@id="{self.test_id}"]{self.attribute}')

    def to_be_visible(self):
        step = f"Check {self.type_of}: {self.name} to be visible"
        with allure.step(step):
            locator = self.get_locator()
            logger.info(step)
            expect(locator).to_be_visible()

    def to_have_text(self, text:str):
        step = f"Check {self.type_of}: {self.name} to have {text}"
        with allure.step(step):
            locator = self.get_locator()
            logger.info(step)
            expect(locator).to_have_text(text)