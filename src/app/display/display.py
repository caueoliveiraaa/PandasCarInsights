"""
Arquivo responsável pela classe Display e os métodos responsáveis pelos logs.
"""

from datetime import date
from logging import DEBUG, FileHandler, Formatter, Logger, getLogger
from os import makedirs, path
from pathlib import Path
from traceback import print_exception

from beartype import beartype

from app.core.caminhos import DIR_LOGS


class Display:
    """
    Classe responsável por imprimir mensagens via print como também via 'Logger'.
    """

    @beartype
    def __init__(self, logger: Logger) -> None:
        """
        Construtor que recebe logger para utilizar a instância e registrar mensagens.
        """
        self.logger: Logger = logger

    @beartype
    def info(self, mensagem: str) -> None:
        """
        Imprime mensagem customizável via print e também via 'logger.info'.
        """
        print(mensagem)
        self.logger.info(mensagem)

    @beartype
    def warning(self, mensagem: str) -> None:
        """
        Imprime mensagem customizável via print e também via 'logger.warning'.
        """
        print(mensagem)
        self.logger.warning(mensagem)

    @beartype
    def error(self, excecao: Exception, mensagem: str = "") -> None:
        """
        Imprime mensagem customizável do erro, em seguida imprime os detalhes
        do erro via 'print_exception' para então registrar o erro via logger também.
        """
        if mensagem:
            mensagem_completa = f"{type(excecao)} {mensagem} {excecao}".strip()
        else:
            mensagem_completa = f"{type(excecao)} - {excecao}".strip()

        print_exception(type(excecao), excecao, excecao.__traceback__)
        self.logger.error(mensagem_completa)


@beartype
def gera_display(processo: str, caminho: Path = DIR_LOGS) -> Display:
    """
    Cria instância de Logger e cria instância de Display passando o logger
    como argumento, para armazenar os logs no caminho definido.
    """
    logger_formatter: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    caminho_completo: str = path.join(caminho, f"{date.today()}.log")
    makedirs(path.dirname(caminho_completo), exist_ok=True)
    logger: Logger = getLogger(processo)

    for handler in logger.handlers:
        logger.removeHandler(handler)

    if not logger.handlers:
        logger.setLevel(level=DEBUG)
        file_handler: FileHandler = FileHandler(caminho_completo)
        formatter: Formatter = Formatter(logger_formatter)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return Display(logger)
