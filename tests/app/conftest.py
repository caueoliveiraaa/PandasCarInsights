"""
Configurações globais de teste e fixtures para todos os testes.
"""

from collections.abc import Generator
from unittest.mock import MagicMock, mock_open, patch

import pytest

from app.database.administrador_banco import AdministradorBanco
from app.schemas.conexao_banco import ConexaoBanco


@pytest.fixture(autouse=True)
def mock_sleep() -> Generator[MagicMock, None, None]:
    """
    Desativa o time.sleep por um mock que não faz nada para performance.
    """
    with patch("time.sleep", return_value=None) as _mock:
        yield _mock


@pytest.fixture(autouse=True)
def mock_print() -> Generator[MagicMock, None, None]:
    """
    Desativa prints em todos os testes para performance.
    """
    with patch("builtins.print") as _mock:
        yield _mock


@pytest.fixture
def mock_db_admin() -> MagicMock:
    """
    Gera um Mock para o AdministradorBanco.
    """
    admin = MagicMock(spec=AdministradorBanco)
    admin.fabrica_dados_conexao.return_value = MagicMock()
    admin.fabrica_engine.return_value = MagicMock()

    return admin


@pytest.fixture
def dados_conexao() -> ConexaoBanco:
    """
    Gera um DTO de conexão mockado para testes de engine.
    """
    return ConexaoBanco(
        usuario="user",
        senha="password",
        servidor="localhost",
        porta=111,
        base="test_db",
        query_driver="driver",
        driver_name="mssql",
    )


@pytest.fixture
def mock_open_file() -> Generator[MagicMock, None, None]:
    """
    Gera um mock do builtins.open globalmente para o teste.
    """
    _mock = mock_open()
    with patch("builtins.open", _mock):
        yield _mock
