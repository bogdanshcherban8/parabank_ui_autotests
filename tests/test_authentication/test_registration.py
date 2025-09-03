import allure
import pytest
from allure_commons.types import Severity

from config import settings
from pages.index_page.index_page import IndexPage
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory


@allure.sub_suite(AllureStory.REGISTRATION)
@allure.suite(AllureFeature.AUTHENTICATION)
@allure.parent_suite(AllureEpic.UI)
@allure.story(AllureStory.REGISTRATION)
@allure.feature(AllureFeature.AUTHENTICATION)
@allure.epic(AllureEpic.UI)
@pytest.mark.authentication
@pytest.mark.smoke
class TestRegistration:
    @allure.severity(Severity.BLOCKER)
    @pytest.mark.positive
    @allure.title("User successfully registrate account")
    def test_registration(self, index_page: IndexPage):
        index_page.visit(f"{settings.http_data.url}{settings.http_data.parabank}/index.htm")
        index_page.left_panel_component.check_visible_left_panel()
