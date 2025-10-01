from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        extra='ignore'
    )
    data_dir : str
    base_model_id : str

    device :str

    WANDB_API_KEY : str
    HF_API_KEY : str


def get_settings() -> Settings:
    """
    Load and return the application settings.
    """
    return Settings()