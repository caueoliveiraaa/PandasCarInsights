"""
Testes para o decorador que captura erros (captura_erros).
"""

from unittest.mock import MagicMock

from app.display.display import Display
from app.middleware.capturador_erros import captura_erros


def retorna_texto() -> str:
    """
    Retorna texto para testar o decorador.
    """
    return "ok"


def lanca_erro(display: Display | None = None) -> None:
    """
    Lança erro para testar o decorador.
    """
    raise RuntimeError()


def test_decorador_retorna_funcao() -> None:
    """
    Valida se o decorador retorna uma função decoradora válida.
    """
    decorador = captura_erros()

    resultado = decorador(retorna_texto)

    assert callable(resultado) is True


def test_executor_seguro_retorna_valor_original() -> None:
    """
    Valida se o retorno da função original é preservado.
    """
    decorador = captura_erros()
    funcao_decorada = decorador(retorna_texto)

    resultado = funcao_decorada()

    assert resultado == "ok"


def test_executor_seguro_lanca_erro_false() -> None:
    """
    Valida se o decorador captura a exceção com sucesso e impede a interrupção
    da thread do script, retornando None.
    """
    decorador = captura_erros()
    funcao_decorada = decorador(lanca_erro)

    resultado = funcao_decorada()

    assert resultado is None


def test_executor_seguro_usa_display() -> None:
    """
    Garante que se um objeto Display for injetado via kwargs, o método error
    será devidamente invocado com a exceção disparada.
    """
    mock_display = MagicMock(spec=Display)
    decorador = captura_erros()
    funcao_decorada = decorador(lanca_erro)

    funcao_decorada(display=mock_display)

    mock_display.error.assert_called_once()


def test_executor_seguro_recorre_ao_print(
    mock_print: MagicMock,
) -> None:
    """
    Garante que se nenhum display for repassado via kwargs, o decorador faz a
    saída do erro de forma resiliente via print tradicional do sistema.
    """
    decorador = captura_erros()
    funcao_decorada = decorador(lanca_erro)

    funcao_decorada()

    mock_print.assert_called_once()
