"""
Mapa das exceções que são utilizadas pelo capturador de erros no módulo middleware.
"""

from email.errors import MessageError
from smtplib import SMTPException

from pydantic import PydanticUserError, ValidationError
from sqlalchemy.exc import SQLAlchemyError

from app.errors.configuracao_invalida import InvalidConfigError


MAPA_EXCECOES: dict[type[BaseException], str] = {
    InvalidConfigError: "Erro na configuração do projeto: ",
    FileNotFoundError: "Arquivo obrigatório não encontrado: ",
    OSError: "Erro ao manipular arquivos: ",
    ModuleNotFoundError: "Módulo necessário não foi encontrado: ",
    UnicodeDecodeError: "Erro de codificação/leitura de texto: ",
    PermissionError: "Permissão insuficiente para executar a operação: ",
    ImportError: "Falha ao carregar dependências do projeto: ",
    ValueError: "Valor inválido: ",
    TypeError: "Tipo de dado incorreto: ",
    KeyError: "Chave inexistente ao acessar dados: ",
    AttributeError: "Atributo inexistente ao acessar dados: ",
    AssertionError: "Falha em uma asserção lógica: ",
    ZeroDivisionError: "Tentativa de divisão por zero: ",
    IndexError: "Índice fora de alcance: ",
    ConnectionError: "Falha de conexão com serviço externo: ",
    RuntimeError: "Erro de execução inesperado: ",
    SQLAlchemyError: "Erro com o banco de dados - SQLAlchemy: ",
    MessageError: "Erro relacionado ao envio ou processamento de mensagens: ",
    SMTPException: "Erro ao enviar email via SMTP: ",
    ValidationError: "Erro de validação de dados (Pydantic): ",
    PydanticUserError: "Erro de definição nos modelos de dados: ",
}
