"""
DTO utilizada para interações com o banco de dados.
"""

from pydantic import BaseModel, ConfigDict, Field


class ConexaoBanco(BaseModel):
    """
    Objeto de valor que armazena os dados necessários para a construção
    de strings de conexão com bases de dados SQL.
    """

    model_config = ConfigDict(frozen=True, str_strip_whitespace=True)

    usuario: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Nome do usuário para autenticação no banco de dados",
    )

    senha: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Senha do usuário para autenticação",
    )

    servidor: str = Field(
        ...,
        min_length=1,
        max_length=100,
        description="Endereço (Hostname ou IP) do servidor de banco de dados",
    )

    base: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Nome da base de dados (Schema) a ser acessada",
    )

    porta: int = Field(
        ...,
        gt=0,
        description="Porta de conexão do serviço de banco de dados",
    )

    query_driver: str = Field(
        default="ODBC Driver 17 for SQL Server",
        description="Nome exato do driver ODBC instalado no sistema operacional",
    )

    driver_name: str = Field(
        default="mssql",
        description="Dialeto do SQLAlchemy a ser utilizado (ex: mssql, postgresql)",
    )
