"""
Exemplo de execução de regra de negócio.
"""

from beartype import beartype

from app.interfaces.exemplo_service import IExemploService


class ExemploService(IExemploService):
    """
    Exemplo de classe para armazenamento de regra de negócio.
    """

    @beartype
    def __init__(self, valor_a: int) -> None:
        """
        Exemplifica inicialização do construtor.
        """
        self._valor_a = valor_a

    @beartype
    def executa_regra_negocio(self, valor_b: int) -> int:
        """
        Exemplifica a execução da regra de negócio.
        """

        return self._valor_a + valor_b
