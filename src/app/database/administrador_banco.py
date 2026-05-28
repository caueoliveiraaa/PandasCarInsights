"""
Cria sessões que lidam com as conexões das bases de dados, permitindo interagir com
tabelas em bases distintas, previamente configuradas.
"""

from collections.abc import Callable, Generator
from contextlib import contextmanager

from beartype import beartype
from sqlalchemy import create_engine, engine
from sqlalchemy.engine import URL, Engine
from sqlalchemy.orm import Session, sessionmaker

from app.core.settings import settings
from app.errors.configuracao_invalida import InvalidConfigError
from app.interfaces.administrador_banco import IAdministradorBanco
from app.schemas.conexao_banco import ConexaoBanco


class AdministradorBanco(IAdministradorBanco):
    """
    Gerenciador de conexões com banco de dados.

    Esta classe centraliza a lógica de criação de engines, conexões e sessões,
    permitindo que diferentes partes da aplicação solicitem conexões de forma
    padronizada.
    """

    @beartype
    def fabrica_engine(self, dados_conexao: ConexaoBanco) -> Engine:
        """
        Cria e configura uma instância da Engine.
        """
        engine_url: URL = engine.URL.create(
            drivername=dados_conexao.driver_name,
            username=dados_conexao.usuario,
            password=dados_conexao.senha,
            host=dados_conexao.servidor,
            port=dados_conexao.porta,
            database=dados_conexao.base,
            query={"driver": dados_conexao.query_driver},
        )
        engine_instancia: Engine = create_engine(
            engine_url,
            echo=False,
            fast_executemany=True,
        )

        return engine_instancia

    @beartype
    def fabrica_dados_conexao(self, nome_conexao: str) -> ConexaoBanco:
        """
        Fabrica os metadados de conexão baseados no nome da base.
        """
        match nome_conexao.lower():
            case "execucoes":
                return ConexaoBanco(
                    usuario=settings.USUARIO_LOCAL,
                    senha=settings.SENHA_LOCAL,
                    servidor=settings.SERVIDOR_LOCAL,
                    porta=settings.PORTA_LOCAL,
                    base=settings.BASE_EXECUCOES,
                )
            case _:
                raise InvalidConfigError(
                    f"Base de dados '{nome_conexao}' não configurada."
                )

    @beartype
    def fabrica_sessao(self, nome_conexao: str) -> Session:
        """
        Cria uma nova sessão para a base informada.
        """
        dados_conexao: ConexaoBanco = self.fabrica_dados_conexao(nome_conexao)
        instancia_engine: Engine = self.fabrica_engine(dados_conexao)
        fabrica_sessao: Callable[[], Session] = sessionmaker(
            bind=instancia_engine, expire_on_commit=False
        )

        return fabrica_sessao()

    @beartype
    @contextmanager
    def abre_sessao(self, nome_conexao: str) -> Generator[Session, None, None]:
        """
        Abre a sessão do SQLAlchemy, garantindo que o commit e o close sejam
        executados e que ocorra rollback em caso de erros.

        Ideal para utilizar com o comando 'with' do Python (via Context Manager).
        """
        sessao: Session = self.fabrica_sessao(nome_conexao)
        try:
            yield sessao
            sessao.commit()
        except Exception as e:
            sessao.rollback()
            raise RuntimeError(
                f"Falha na transação da base '{nome_conexao}': {e}"
            ) from e
        finally:
            sessao.close()
