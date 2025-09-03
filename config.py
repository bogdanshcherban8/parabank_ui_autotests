from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import DirectoryPath, BaseModel, HttpUrl
from typing import Self, List


class HttpDataConfig(BaseModel):
    base_url: HttpUrl
    browsers: List[str]
    headless: bool
    parabank: str

    @property
    def url(self) -> str:
        return str(self.base_url)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", env_nested_delimiter=".")
    allure_results_dir: DirectoryPath
    http_data: HttpDataConfig
    tracing_dir: DirectoryPath
    record_video_dir: DirectoryPath

    @classmethod
    def initialize(cls) -> Self:
        allure_results_dir = DirectoryPath("./allure-results")
        allure_results_dir.mkdir(exist_ok=True)
        record_video_dir = DirectoryPath("./record_video_dir")
        record_video_dir.mkdir(exist_ok=True)
        tracing_dir = DirectoryPath("./tracing_dir")
        tracing_dir.mkdir(exist_ok=True)
        return Settings(allure_results_dir=allure_results_dir, record_video_dir=record_video_dir,
                        tracing_dir=tracing_dir)


settings = Settings.initialize()
