"""Entry point of the project."""

from os import name as os_name
from os import system

from src.services.containers import CarDataAnalysisContainer
from src.shared.error_handling import error_handler


@error_handler
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
    car_container = CarDataAnalysisContainer()
    car_analyzer = car_container.car_data_analysis()
    car_analyzer.display_main_menu()


if __name__ == "__main__":
    main()
