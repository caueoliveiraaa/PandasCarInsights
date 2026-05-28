"""
Gerenciador de execuções dos scripts, com logs e validação de horários.
"""

from datetime import date, datetime
from locale import LC_TIME, setlocale
from time import sleep

from app.database.administrador_banco import AdministradorBanco
from app.display.display import Display, gera_display

from app.scripts.exemplo_script import exemplo_script

setlocale(LC_TIME, "pt_BR.UTF-8")


def main() -> None:
    """
    Organiza a chamada dos scripts e garante que os mesmos sejam executados
    em datas/horários específicos e com monitoramento via base Execucoes.
    """
    db_admin = AdministradorBanco()
    display: Display = gera_display("processo")
    ultimo_update: date = datetime.now().date()

    while True:
        agora: datetime = datetime.now()
        if agora.date() > ultimo_update:
            display = gera_display("processo")
            ultimo_update = agora.date()

        exemplo_script(display=display)
        display.info("Ativo")
        sleep(30)
