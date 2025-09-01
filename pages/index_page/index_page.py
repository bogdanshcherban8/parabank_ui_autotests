from components.leftpanel.leftpanel import LeftPanel
from components.rightpanel.rightpanel import RightPanel
from pages.base_page import BasePage
from playwright.sync_api import Page

class IndexPage(BasePage):
    def __init__(self, page:Page):
        super().__init__(page)
        self.left_panel_component=LeftPanel(page)
        self.right_panel_component=RightPanel(page)
