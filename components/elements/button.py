import allure

from components.elements.base_element import BaseElement, logger
from playwright.sync_api import expect

class Button(BaseElement):
    @property
    def type_of(self)->str:
        return "button"

    def to_have_value(self, value:str):
        step=f"Expected that {self.type_of}: {self.name} have value"
        with allure.step(step):
            locator=self.get_locator()
            logger.info(step)
            expect(locator).to_have_value(value)