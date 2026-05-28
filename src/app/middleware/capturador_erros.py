"""
Decorador utilizado para padronizar o tratamento de exceções em funções de
alto nível (funções orquestradoras).
"""

from collections.abc import Callable
from functools import wraps
from typing import ParamSpec, TypeVar

from app.core.middleware import MAPA_EXCECOES
from app.display.display import Display


P = ParamSpec("P")
R = TypeVar("R")


def captura_erros() -> Callable[[Callable[P, R]], Callable[P, R | None]]:
    """
    Captura exceções comuns, registrar via display.error e opcionalmente relança
    as exceções capturadas.
    """

    def decorador(funcao: Callable[P, R]) -> Callable[P, R | None]:
        """
        Aplica o tratamento de erros à função alvo.
        """

        @wraps(funcao)
        def executor_seguro(*args: P.args, **kwargs: P.kwargs) -> R | None:
            """
            Executa a função decorada dentro de um bloco seguro, capturando
            exceções definidas na constante MAPA_EXCECOES.
            """
            try:
                return funcao(*args, **kwargs)
            except Exception as excecao:
                mensagem: str = MAPA_EXCECOES.get(type(excecao), "Erro inesperado: ")
                display: object | None = kwargs.get("display")

                if display and isinstance(display, Display):
                    display.error(excecao, mensagem)
                else:
                    print(mensagem, excecao)

                return None

        return executor_seguro

    return decorador
