"""
Testes para a lógica de exemplo_script.
"""

from unittest.mock import MagicMock

from app.display.display import Display
from app.scripts.exemplo_script import exemplo_script


def test_exemplo_script(mock_executor: MagicMock) -> None:
    """
    Garante que o método executa_regra_negocio() finaliza corretamente e
    aciona o executor.
    """
    mock_display = MagicMock(spec=Display)

    resultado = exemplo_script(mock_display)

    assert resultado is True
    mock_executor.executa_regra_negocio.assert_called_once_with(valor_b=20)
    mock_display.info.assert_called_once()


def test_exemplo_script_sem_display(
    mock_executor: MagicMock, mock_gera_display: MagicMock
) -> None:
    """
    Garante que o método executa_regra_negocio() finaliza corretamente e
    aciona o executor.
    """
    mock_display = MagicMock(spec=Display)
    mock_gera_display.return_value = mock_display

    resultado = exemplo_script(None)

    assert resultado is True
    mock_executor.executa_regra_negocio.assert_called_once_with(valor_b=20)
    mock_gera_display.assert_called_once()
    mock_display.info.assert_called_once()
