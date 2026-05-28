"""
Armazena a interface de contrato para a lógica da classe AdministradorBanco.
"""

from abc import ABC, abstractmethod
from collections.abc import Generator
from contextlib import contextmanager

from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session

from app.schemas.conexao_banco import ConexaoBanco


class IAdministradorBanco(ABC):
    """
    Interface que define o contrato para o gerenciamento de conexões e sessões
    síncronas de banco de dados.
    """

    @abstractmethod
    def fabrica_engine(self, dados_conexao: ConexaoBanco) -> Engine:
        """
        Contrato para criação e configuração de instâncias de Engine.
        """
        pass

    @abstractmethod
    def fabrica_dados_conexao(self, nome_conexao: str) -> ConexaoBanco:
        """
        Contrato para obtenção dos metadados de conexão baseados no nome da base.
        """
        pass

    @abstractmethod
    def fabrica_sessao(self, nome_conexao: str) -> Session:
        """
        Contrato para criação de uma nova sessão para a base informada.
        """
        pass

    @abstractmethod
    @contextmanager
    def abre_sessao(self, nome_conexao: str) -> Generator[Session, None, None]:
        """
        Contrato para o gerenciador de contexto que orquestra a sessão.
        """
        pass
