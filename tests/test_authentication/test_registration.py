import allure

from pages.index_page.index_page import IndexPage
from config import settings
from tools.routes import Routes
import pytest


@pytest.mark.registration
@pytest.mark.authentication
@pytest.mark.smoke
@allure.title("Successful user registration")
class TestRegistration:
    def test_registration(self, index_page: IndexPage):
        index_page.visit(f"{settings.http_data.base_url}{Routes.PARABANK.value}/index.htm")
        index_page.left_panel_component.check_visible()
        index_page.left_panel_component.check_have_text()
        index_page.left_panel_component.check_have_value()
        index_page.left_panel_component.check_enabled()
        index_page.left_panel_component.check_have_attribute()
        index_page.left_panel_component.check_clicking_register_button()

        index_page.right_panel_component.check_visible_customer_form()
        index_page.right_panel_component.check_have_text_customer_form()
        index_page.right_panel_component.check_have_value_customer_form()
        index_page.right_panel_component.check_enabled_customer_form()
        index_page.right_panel_component.check_filling_customer_form()
        index_page.right_panel_component.check_clicking_register_button()

        index_page.right_panel_component.check_visible_right_panel()
        index_page.right_panel_component.check_have_text_right_panel()




