"""
Configurações globais de teste e fixtures para testes do módulo scripts.
"""

from collections.abc import Generator
from unittest.mock import MagicMock, patch

import pytest


@pytest.fixture
def mock_executor() -> Generator[MagicMock, None, None]:
    """
    Simula o executor de lógica de negócio para isolar testes de script.
    """
    with patch("app.scripts.exemplo_script.ExemploService") as mocked:
        instancia = mocked.return_value
        instancia.executa_regra_negocio.return_value = 30

        yield instancia


@pytest.fixture
def mock_gera_display() -> Generator[MagicMock, None, None]:
    """
    Simula a função que gera a instância do display para logs.
    """
    with patch("app.scripts.exemplo_script.gera_display") as mocked:
        yield mocked
