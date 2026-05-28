"""
Classe que representa uma exceção de configuração inválida.
"""


class InvalidConfigError(Exception):
    """
    Exceção para configuração inválida identificada.
    """

    def __init__(self, message: str = "A configuração fornecida é inválida") -> None:
        """
        Inicializa a exceção com uma mensagem padrão.
        """
        super().__init__(message)
