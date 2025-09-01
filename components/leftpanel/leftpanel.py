import re

from components.base_component import BaseComponent
from playwright.sync_api import Page

from components.elements.input import Input
from components.elements.text import Text
from components.elements.button import Button
from components.elements.link import Link
from config import settings
from tools.routes import Routes


class LeftPanel(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title_main = Text(page, "leftPanel", "//h2", "Customer Login title")
        self.title_username = Text(page, "loginPanel", "//p[1]/b", "Username title")
        self.input_username = Input(page, "loginPanel", "//div[1]/input", "Username input")
        self.title_password = Text(page, "loginPanel", "//p[2]/b", "Password title")
        self.input_password = Input(page, "loginPanel", "//div[2]/input", "Password input")
        self.button_log_in = Button(page, "loginPanel", "//div[3]/input", "LOG IN button")
        self.button_forgot_login = Link(page, "loginPanel", "//p[1]/a", "Forgot login info? button")
        self.button_register = Link(page, "loginPanel", "//p[2]/a", "Register button")

    def check_visible(self):
        self.check_url("index.htm")
        self.title_main.to_be_visible()
        self.title_username.to_be_visible()
        self.input_username.to_be_visible()
        self.title_password.to_be_visible()
        self.input_password.to_be_visible()
        self.button_log_in.to_be_visible()
        self.button_forgot_login.to_be_visible()
        self.button_register.to_be_visible()

    def check_have_text(self):
        self.title_main.to_have_text("Customer Login")
        self.title_username.to_have_text("Username")
        self.title_password.to_have_text("Password")
        self.button_forgot_login.to_have_text("Forgot login info?")
        self.button_register.to_have_text("Register")

    def check_have_value(self):
        self.button_log_in.to_have_value("Log In")

    def check_have_attribute(self):
        self.button_forgot_login.to_have_attribute("href", f"lookup.htm")
        self.button_register.to_have_attribute("href", "register.htm")

    def check_enabled(self):
        self.button_log_in.to_be_enabled()
        self.input_username.to_be_enabled()
        self.input_password.to_be_enabled()

    def check_clicking_log_in(self):
        self.button_log_in.click()

    def check_clicking_register_button(self):
        self.button_register.click()

    def check_clicking_forgot_login(self):
        self.button_forgot_login.click()

    def check_filling(self):
        self.input_username.fill(self.fake.email())
        self.input_password.fill(self.fake.password())

    def check_url(self, expected_url: str):
        return self.check_current_url(
            re.compile(rf"{settings.http_data.base_url}{Routes.PARABANK.value}/{expected_url}"))
