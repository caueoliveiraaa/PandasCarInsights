"""
Exemplo de implementação de um script.
"""

from app.display.display import Display, gera_display
from app.middleware.capturador_erros import captura_erros
from app.services.exemplo_service import ExemploService


@captura_erros()
def exemplo_script(display: Display | None = None) -> bool | None:
    """
    Executor de exemplo para ScriptExemplo

    Garante integração com o decorador captura_erros para não encerrar execuções
    quando houver erros.
    """
    if display is None:
        display = gera_display("processo")

    executou = False
    executor = ExemploService(valor_a=10)

    resultado: int = executor.executa_regra_negocio(valor_b=20)
    display.info(f"Resultado do processo: {resultado}.")
    executou = True

    return executou


# TODO: Permitir conexões com bancos diferentes
# TODO: Remover dirs do vulture
# TODO: Refatorar configuração e estrutura