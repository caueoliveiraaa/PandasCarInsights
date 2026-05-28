"""
Testes para a classe Executor.
"""

from app.services.exemplo_service import ExemploService


def test_init_executor() -> None:
    """
    Valida a inicialização do construtor.
    """
    valor_a = 10

    exec = ExemploService(valor_a)

    assert exec._valor_a == valor_a


def test_executa_regra_negocio() -> None:
    """
    Valida a execução do cálculo do método executa_regra_negocio.
    """
    valor_a = 10
    valor_b = 5
    exec = ExemploService(valor_a)

    resultado = exec.executa_regra_negocio(valor_b)

    assert resultado == (valor_a + valor_b)
