from config import settings
import pytest
def create_allure_environment_file():
    items = [f'{key}={value}' for key, value in settings.model_dump().items()]
    properties = '\n'.join(items)
    with open(settings.allure_results_dir.joinpath("environment_properties"), "w+") as file:
        file.write(properties)

@pytest.fixture(scope="session", autouse=True)
def save_allure_environment_file():
    yield
    create_allure_environment_file()