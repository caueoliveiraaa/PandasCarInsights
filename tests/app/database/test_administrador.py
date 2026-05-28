"""
Testes para a classe AdministradorBanco.
"""

from unittest.mock import MagicMock

import pytest
from sqlalchemy.orm import Session

from app.database.administrador_banco import AdministradorBanco
from app.errors.configuracao_invalida import InvalidConfigError
from app.schemas.conexao_banco import ConexaoBanco


def test_fabrica_engine(
    mock_sqlalchemy_engine: MagicMock,
    dados_conexao: ConexaoBanco,
    adm_banco: AdministradorBanco,
) -> None:
    """
    Garante a criação da engine com os parâmetros corretos.
    """
    engine = adm_banco.fabrica_engine(dados_conexao)

    assert mock_sqlalchemy_engine.called
    args, kwargs = mock_sqlalchemy_engine.call_args
    assert kwargs["fast_executemany"] is True
    assert kwargs["echo"] is False
    assert engine == mock_sqlalchemy_engine.return_value


def test_fabrica_dados_conexao(adm_banco: AdministradorBanco) -> None:
    """
    Garante o mapeamento 'execucoes' retorna um DTO ConexaoBanco.
    """
    dados = adm_banco.fabrica_dados_conexao("execucoes")

    assert isinstance(dados, ConexaoBanco)
    assert dados.base is not None


def test_fabrica_dados_conexao_erro(adm_banco: AdministradorBanco) -> None:
    """
    Garante que um erro é disparado para bases não mapeadas.
    """
    with pytest.raises(InvalidConfigError, match="não configurada"):
        adm_banco.fabrica_dados_conexao("base_inexistente")


def test_fabrica_sessao(
    mock_sessionmaker: MagicMock,
    mock_sqlalchemy_engine: MagicMock,
    mock_adm_fabrica_dados: MagicMock,
    adm_banco: AdministradorBanco,
) -> None:
    """
    Garante que a fábrica de sessão retorna uma instância de Session.
    """
    sessao = adm_banco.fabrica_sessao("execucoes")

    assert isinstance(sessao, Session)


def test_abre_sessao_executa_commit(
    mock_sessionmaker: MagicMock,
    mock_adm_fabrica_sessao: MagicMock,
    adm_banco: AdministradorBanco,
) -> None:
    """
    Garante o fluxo do context manager (commit e close).
    """
    with adm_banco.abre_sessao("execucoes") as sessao:
        sessao.add(MagicMock())

    mock_sessionmaker.commit.assert_called_once()
    mock_sessionmaker.close.assert_called_once()


def test_abre_sessao_executa_rollback(
    mock_sessionmaker: MagicMock,
    mock_adm_fabrica_sessao: MagicMock,
    adm_banco: AdministradorBanco,
) -> None:
    """
    Garante que o rollback é acionado quando ocorre um erro dentro do bloco.
    """
    with pytest.raises(RuntimeError, match="Falha na transação"):
        with adm_banco.abre_sessao("execucoes") as _sessao:
            raise RuntimeError("Falha na transação")

    mock_sessionmaker.commit.assert_not_called()
    mock_sessionmaker.close.assert_called_once()
    mock_sessionmaker.rollback.assert_called_once()
