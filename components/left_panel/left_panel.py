import re

from components.base_component import BaseComponent
from playwright.sync_api import Page
from components.elements.text import Text
from config import settings


class LeftPanel(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title_customer_login = Text(page, "leftPanel", "//h2", "Customer Login")

    def check_visible_left_panel(self):
        self.check_url("/index.htm")
        self.title_customer_login.to_be_visible()

    def check_url(self, endpoint: str):
        return self.check_current_url(re.compile(f"{settings.http_data.url}{settings.http_data.parabank}{endpoint}"))
