"""Entry point of the project."""

from logging import Logger
from os import name as os_name
from os import system

from rich.errors import ConsoleError, StyleError

from src.services.script_analyze_car_data import CarDataAnalysis
from src.shared.base_logger import BaseLogger
from src.shared.rich_printer import RichPrinter


def main() -> None:
    """Method responsible for executing the program.

    Raises:
        OSError: If an error occurs when handling the json file.
        ValueError: If there is a problem with the value in the json.
        TypeError: If the json contains unexpected types.
        ConsoleError: If an error occurs in console operation.
        StyleError: If an error occurs when applying styles.
    """
    system("cls" if os_name == "nt" else "clear")
    base_logger: BaseLogger = BaseLogger()
    main_logger: Logger = base_logger.get_logger()

    try:
        car_analyzer: CarDataAnalysis = CarDataAnalysis(
            logger=base_logger.get_logger(), rich=RichPrinter()
        )
        car_analyzer.analyze_car_data()
    except OSError as e:
        main_logger.error(e)
    except ValueError as e:
        main_logger.error(e)
    except TypeError as e:
        main_logger.error(e)
    except ConsoleError as e:
        main_logger.error(e)
    except StyleError as e:
        main_logger.error(e)


if __name__ == "__main__":
    main()
