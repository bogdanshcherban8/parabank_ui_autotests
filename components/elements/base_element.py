from playwright.sync_api import Page, expect

from tools.jsessionid import get_jsessionid
from tools.logger import get_logger
import allure

logger = get_logger("BASE_ELEMENT")


class BaseElement:
    def __init__(self, page: Page, test_id: str, sub_attribute: str, name: str):
        self.page = page
        self.test_id = test_id
        self.sub_attribute = sub_attribute
        self.name = name

    @property
    def type_of(self) -> str:
        return "base element"

    def get_locator(self):
        step = f"Get locator from id: {self.test_id} and {self.sub_attribute}"
        with allure.step(step):
            logger.info(step)
            return self.page.locator(f'//*[@id="{self.test_id}"]{self.sub_attribute}')

    def to_be_visible(self):
        step = f"Expected that {self.type_of}: {self.name} to be visible"
        with allure.step(step):
            locator = self.get_locator()
            logger.info(step)
            expect(locator).to_be_visible()

    def to_have_text(self, text: str):
        step = f"Expected that {self.type_of}: {self.name} have text: {text}"
        with allure.step(step):
            locator = self.get_locator()
            logger.info(step)
            expect(locator).to_have_text(text)

    def to_be_enabled(self):
        step = f"Expected that {self.type_of}: {self.name} to be enabled"
        with allure.step(step):
            locator = self.get_locator()
            logger.info(step)
            expect(locator).to_be_enabled()
    def is_visible(self, text:str):
        step = f"Expected that {self.type_of}: {self.name} is visible"
        with allure.step(step):
            locator = self.get_locator()
            logger.info(step)
            try:
                expect(locator).to_have_text(text)
                return True
            except AssertionError:
                return False
    def to_be_disabled(self):
        step = f"Expected that {self.type_of}: {self.name} to be disabled"
        with allure.step(step):
            locator = self.get_locator()
            logger.info(step)
            expect(locator).to_be_disabled()

    def click(self):
        step = f"Clicking {self.type_of}: {self.name}"
        with allure.step(step):
            locator = self.get_locator()
            logger.info(step)
            locator.click()

    def to_have_attribute(self, name: str, value: str):
        step = f"Expected that {self.type_of}: {self.name} have {name}: {value}"
        with allure.step(step):
            locator = self.get_locator()
            jsessionid = get_jsessionid(self.page)
            logger.info(step)
            expect(locator).to_have_attribute(name, f"{value};jsessionid={jsessionid}")
