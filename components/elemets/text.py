from components.elemets.base_element import BaseElement


class Text(BaseElement):
    @property
    def type_of(self):
        return "text"