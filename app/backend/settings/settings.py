from pydantic_settings import BaseSettings, SettingsConfigDict

class EnvSettings(BaseSettings):
    POSTGRESQL_URL: str
    POSTGRESQL_TEST_URL: str

    model_config = SettingsConfigDict(env_file='.env',)


env_settings = EnvSettings()

