"""
Fixtures para testes do módulo middleware.
"""

from collections.abc import Generator
from unittest.mock import MagicMock, patch

import pytest


@pytest.fixture
def mock_print() -> Generator[MagicMock, None, None]:
    """
    Intercepta a o print utilizado no capturador de erros para validar a
    impressão de exceções.
    """
    with patch("app.middleware.capturador_erros.print") as mocked:
        yield mocked
