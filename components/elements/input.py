from components.elements.base_element import BaseElement, logger

import allure


class Input(BaseElement):
    @property
    def type_of(self) -> str:
        return "input"

    def fill(self, text: str):
        step = f"Filling {self.type_of}: {self.name} with {text}"
        with allure.step(step):
            locator = self.get_locator()
            logger.info(step)
            return locator.fill(text)
