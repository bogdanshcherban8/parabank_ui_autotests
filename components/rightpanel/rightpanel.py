import re

from pytest_playwright.pytest_playwright import page

from components.base_component import BaseComponent
from components.elements.input import Input
from components.elements.text import Text
from components.elements.button import Button
from playwright.sync_api import Page

from config import settings
from tools.jsessionid import get_jsessionid
from tools.routes import Routes


class RightPanel(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)
        self.title_main = Text(page, "rightPanel", "//h1", "Signing up is easy! title")
        self.text_paragraph = Text(page, "rightPanel", "//p", "If you have an account text")
        self.title_first_name = Text(page, "customerForm", "//tr[1]//b", "First Name: title")
        self.input_first_name = Input(page, "customerForm", "//tr[1]//input", "First Name: input")
        self.title_last_name = Text(page, "customerForm", "//tr[2]//b", "Last Name: title")
        self.input_last_name = Input(page, "customerForm", "//tr[2]//input", "Last Name: input")
        self.title_address = Text(page, "customerForm", "//tr[3]//b", "Address: title")
        self.input_address = Input(page, "customerForm", "//tr[3]//input", "Address: input")
        self.title_city = Text(page, "customerForm", "//tr[4]//b", "City: title")
        self.input_city = Input(page, "customerForm", "//tr[4]//input", "City: input")
        self.title_state = Text(page, "customerForm", "//tr[5]//b", "State: title")
        self.input_state = Input(page, "customerForm", "//tr[5]//input", "State: input")
        self.title_zip_code = Text(page, "customerForm", "//tr[6]//b", "Zip Code: title")
        self.input_zip_code = Input(page, "customerForm", "//tr[6]//input", "Zip Code: input")
        self.title_phone = Text(page, "customerForm", "//tr[7]//b", "Phone #: title")
        self.input_phone = Input(page, "customerForm", "//tr[7]//input", "Phone #: input")
        self.title_ssn = Text(page, "customerForm", "//tr[8]//b", "SSN: title")
        self.input_ssn = Input(page, "customerForm", "//tr[8]//input", "SSN: input")
        self.title_username = Text(page, "customerForm", "//tr[10]//b", "Username: title")
        self.input_username = Input(page, "customerForm", "//tr[10]//input", "Username: input")
        self.title_password = Text(page, "customerForm", "//tr[11]//b", "Password: title")
        self.input_password = Input(page, "customerForm", "//tr[11]//input", "Password: input")
        self.title_confirm = Text(page, "customerForm", "//tr[12]//b", "Confirm: title")
        self.input_confirm = Input(page, "customerForm", "//tr[12]//input", "Confirm: input")
        self.button_register = Button(page, "customerForm", "//tr[13]//input", "Register button")
        self.title_main_right_panel = Text(page, "rightPanel", "//h1", "Welcome ... title")
        self.text_paragraph_right_panel = Text(page, "rightPanel", "//p", "Your account was created successfully text")
        self.text_username_already_exist = Text(page, "customer.username.errors", "",
                                                "This username already exists. text")

    def check_visible_customer_form(self):
        self.check_url("register.htm")
        self.title_main.to_be_visible()
        self.text_paragraph.to_be_visible()
        self.title_first_name.to_be_visible()
        self.input_first_name.to_be_visible()
        self.title_last_name.to_be_visible()
        self.input_last_name.to_be_visible()
        self.title_address.to_be_visible()
        self.input_address.to_be_visible()
        self.title_city.to_be_visible()
        self.input_city.to_be_visible()
        self.title_state.to_be_visible()
        self.input_state.to_be_visible()
        self.title_zip_code.to_be_visible()
        self.input_zip_code.to_be_visible()
        self.title_phone.to_be_visible()
        self.input_phone.to_be_visible()
        self.title_ssn.to_be_visible()
        self.input_ssn.to_be_visible()
        self.title_username.to_be_visible()
        self.input_username.to_be_visible()
        self.title_password.to_be_visible()
        self.input_password.to_be_visible()
        self.title_confirm.to_be_visible()
        self.input_confirm.to_be_visible()
        self.button_register.to_be_visible()

    def check_visible_right_panel(self):
        self.title_main_right_panel.to_be_visible()
        self.text_paragraph_right_panel.to_be_visible()

    def check_have_text_right_panel(self):
        self.title_main_right_panel.to_have_text(f"Welcome {self.username}")
        self.text_paragraph_right_panel.to_have_text("Your account was created successfully. You are now logged in.")

    def check_clicking_register_button(self, max_attempts: int = 5):
        for attempt in range(max_attempts):
            self.button_register.click()
            if self.text_username_already_exist.is_visible("This username already exists."):
                self.page.context.clear_cookies()
                self.page.goto("https://parabank.parasoft.com/parabank/index.htm")
                self.page.goto("https://parabank.parasoft.com/parabank/register.htm")
                self.check_filling_customer_form()
                continue
            else:
                return
        raise Exception("Internal error")

    def check_have_value_customer_form(self):
        self.button_register.to_have_value("Register")

    def check_enabled_customer_form(self):
        self.input_first_name.to_be_enabled()
        self.input_last_name.to_be_enabled()
        self.input_address.to_be_enabled()
        self.input_city.to_be_enabled()
        self.input_state.to_be_enabled()
        self.input_zip_code.to_be_enabled()
        self.input_phone.to_be_enabled()
        self.input_ssn.to_be_enabled()
        self.input_username.to_be_enabled()
        self.input_password.to_be_enabled()
        self.input_confirm.to_be_enabled()
        self.button_register.to_be_enabled()

    def check_have_text_customer_form(self):
        self.title_main.to_have_text("Signing up is easy!")
        self.text_paragraph.to_have_text(
            "If you have an account with us you can sign-up for free instant online access. You will have to provide some personal information.")
        self.title_first_name.to_have_text("First Name:")
        self.title_last_name.to_have_text("Last Name:")
        self.title_address.to_have_text("Address:")
        self.title_city.to_have_text("City:")
        self.title_state.to_have_text("State:")
        self.title_zip_code.to_have_text("Zip Code:")
        self.title_phone.to_have_text("Phone #:")
        self.title_ssn.to_have_text("SSN:")
        self.title_username.to_have_text("Username:")
        self.title_password.to_have_text("Password:")
        self.title_confirm.to_have_text("Confirm:")

    def check_filling_customer_form(self):
        self.input_first_name.fill(self.fake.first_name())
        self.input_last_name.fill(self.fake.last_name())
        self.input_address.fill(self.fake.address())
        self.input_city.fill(self.fake.city())
        self.input_state.fill(self.fake.state())
        self.input_zip_code.fill(self.fake.zipcode())
        self.input_phone.fill(self.fake.phone_number())
        self.input_ssn.fill(self.fake.ssn())
        username = self.fake.user_name()
        password = self.fake.password()
        self.input_username.fill(username)
        self.input_password.fill(password)
        self.input_confirm.fill(password)
        self.username = username
        self.password = password

    def check_url(self, expected_url: str):
        jsessionid = get_jsessionid(self.page)
        return self.check_current_url(
            re.compile(rf"{settings.http_data.base_url}{Routes.PARABANK.value}/{expected_url};jsessionid={jsessionid}"))
