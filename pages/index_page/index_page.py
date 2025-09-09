from components.left_panel.left_panel import LeftPanel
from pages.base_page import BasePage
from playwright.sync_api import Page

class IndexPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.left_panel_component = LeftPanel(page)
