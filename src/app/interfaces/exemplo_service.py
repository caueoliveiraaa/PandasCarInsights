"""
Armazena a interface de contrato para a lógica da classe ExemploService.
"""

from abc import ABC, abstractmethod


class IExemploService(ABC):
    """
    Interface que define o contrato para classes de execução de regras de negócio.
    """

    @abstractmethod
    def executa_regra_negocio(self, valor_b: int) -> int:
        """
        Contrato para a execução de uma regra de negócio específica.
        """
        pass
