from pydantic import BaseModel, DirectoryPath, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class HttpDataConfig(BaseModel):
    browsers: list[str]
    headless: bool
    parabank: str
    index: str
    base_url: HttpUrl

    @property
    def url(self):
        return str(self.base_url)

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", env_nested_delimiter=".")

    http_data: HttpDataConfig

    tracing: DirectoryPath
    record_video_dir: DirectoryPath
    allure_results_dir: DirectoryPath
    

    @classmethod
    def initialize(cls):
        tracing = DirectoryPath("./tracing")
        tracing.mkdir(exist_ok=True)
        record_video_dir = DirectoryPath("./record_video_dir")
        record_video_dir.mkdir(exist_ok=True)
        allure_results_dir = DirectoryPath("./allure-results")
        return Settings(tracing=tracing, record_video_dir=record_video_dir, allure_results_dir=allure_results_dir)


settings = Settings.initialize()
