import pytest
from allure_commons.types import Severity

from config import settings
from pages.index_page.index_page import IndexPage
import allure

from tools.allure.epics import AllureEpic
from tools.allure.features import AllureStory
from tools.allure.stories import AllureFeature


@allure.suite(AllureFeature.AUTHENTICATION)
@allure.feature(AllureFeature.AUTHENTICATION)
@pytest.mark.authentication
@pytest.mark.smoke
@pytest.mark.registration
class TestAuthentication:
    @allure.severity(Severity.BLOCKER)
    @allure.story(AllureStory.REGISTRATION)
    @allure.sub_suite(AllureStory.REGISTRATION)
    @allure.epic(AllureEpic.POSITIVE)
    @allure.parent_suite(AllureEpic.POSITIVE)
    @pytest.mark.positive
    @allure.title("User successful registration")
    def test_registration(self, index_page: IndexPage):
        index_page.visit(f"{settings.http_data.url}{settings.http_data.parabank}/{settings.http_data.index}")
        index_page.left_panel_component.check_url_left_panel()
        index_page.left_panel_component.check_url_left_panel()
        index_page.left_panel_component.check_have_text_left_panel()
