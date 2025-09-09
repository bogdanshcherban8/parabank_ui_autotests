import re

from components.base_component import BaseComponent
from playwright.sync_api import Page
from components.elemets.text import Text
from config import settings


class LeftPanel(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title_customer_login = Text(page, "leftPanel", "//h2", "Customer login")

    def check_visible_left_panel(self):
        self.title_customer_login.to_be_visible()

    def check_have_text_left_panel(self):
        self.title_customer_login.to_have_text("Customer Login")

    def check_url_left_panel(self):
        self.check_current_url(
            re.compile(rf"{settings.http_data.url}{settings.http_data.parabank}/{settings.http_data.index}"))
