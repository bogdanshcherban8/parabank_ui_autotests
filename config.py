from pydantic import BaseModel, HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class HttpDataConfig(BaseModel):
    base_url: HttpUrl
    browsers: list[str]
    headless: bool
    @property
    def url(self) -> str:
        return str(self.base_url)


class PathDataConfig(BaseModel):
    trace: str


class Settings(BaseSettings):
    model_config=SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", env_nested_delimiter=".")
    http_data: HttpDataConfig
    path_data: PathDataConfig

settings=Settings()

