"""
Fixtures para testes do módulo database.
"""

from collections.abc import Generator
from unittest.mock import MagicMock, patch

import pytest
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from app.database.administrador_banco import AdministradorBanco
from app.schemas.conexao_banco import ConexaoBanco


@pytest.fixture
def mock_sqlalchemy_engine() -> Generator[MagicMock, None, None]:
    """
    Intercepta a criação de engines do SQLAlchemy.
    """
    with patch("app.database.administrador_banco.create_engine") as mocked:
        mock_engine = MagicMock(spec=Engine)
        mocked.return_value = mock_engine
        yield mocked


@pytest.fixture
def mock_sessionmaker() -> Generator[MagicMock, None, None]:
    """
    Intercepta o sessionmaker para retornar uma sessão mockada.
    """
    with patch("app.database.administrador_banco.sessionmaker") as mocked_factory:
        mock_sessao = MagicMock(spec=Session)
        mocked_factory.return_value.return_value = mock_sessao
        yield mock_sessao


@pytest.fixture
def adm_banco() -> AdministradorBanco:
    """
    Gera uma instância básica do AdministradorBanco para ser usada nos patches.
    """
    return AdministradorBanco()


@pytest.fixture
def mock_adm_fabrica_dados(
    adm_banco: AdministradorBanco, dados_conexao: ConexaoBanco
) -> Generator[MagicMock, None, None]:
    """
    Intercepta o método fabrica_dados_conexao da instância do AdministradorBanco.
    """
    with patch.object(
        adm_banco, "fabrica_dados_conexao", return_value=dados_conexao
    ) as mocked:
        yield mocked


@pytest.fixture
def mock_adm_fabrica_sessao(
    adm_banco: AdministradorBanco, mock_sessionmaker: MagicMock
) -> Generator[MagicMock, None, None]:
    """
    Intercepta o método fabrica_sessao para retornar o mock da sessão.
    """
    with patch.object(
        adm_banco, "fabrica_sessao", return_value=mock_sessionmaker
    ) as mocked:
        yield mocked
