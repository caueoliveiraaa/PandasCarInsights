"""
Informações que não devem ser alteradas e que são sensíveis, como credenciais,
emails, tokens, e quaisquer dados sensíveis.
"""

from dotenv import load_dotenv
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class Settings(BaseSettings):
    """
    Classe responsável por administrar as variáveis de ambiente.
    """

    USUARIO_LOCAL: str = Field(default="usuario_temp")
    SENHA_LOCAL: str = Field(default="senha_temp")
    SERVIDOR_LOCAL: str = Field(default="servidor_temp")
    PORTA_LOCAL: int = Field(default=1111)
    BASE_EXECUCOES: str = Field(default="base_temp")

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()
