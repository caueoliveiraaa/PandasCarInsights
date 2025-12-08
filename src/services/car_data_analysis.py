"""Read data from 'car_dataset.json', clean the data acquired, organaze and view
it by applying data analysis techniques to get insights about the car data.
"""

from os import name as os_name
from os import system

from beartype import beartype
from pandas import DataFrame
from rich.rule import Rule
from rich.table import Table

from src.domain.car_data_analysis import CarAnalysisDependencies
from src.interfaces.services.dataframe_analyzer_interface import IDataFrameAnalyzer
from src.interfaces.services.dataframe_cleaner_interface import IDataFrameCleaner
from src.interfaces.services.dataset_loader_interface import IDataSetLoader
from src.interfaces.shared.logger_interface import ILogger
from src.interfaces.shared.rich_printer_interface import IRichPrinter
from src.shared.error_handling import error_handler


class CarDataAnalysis:
    """Orchestrate the logic for analyzing data from 'car_dataset.json'."""

    @beartype
    def __init__(self, dependencies: CarAnalysisDependencies) -> None:
        """Initialize the 'CarDataAnalysis' orchestrator.

        Args:
            dependencies: Bundle containing loader, cleaner, analyzer, logger,
                and printer instances.

        Attributes:
            _loader: Service for loading datasets.
            _cleaner: Service for cleaning dataframes.
            _analyzer: Service for analyzing dataframes.
            _logge: Logger instance for logging information.
            _printer: Printer instance for styled console output.
            _car_dataset: The loaded car dataset.
        """
        self._loader: IDataSetLoader = dependencies.loader
        self._cleaner: IDataFrameCleaner = dependencies.cleaner
        self._analyzer: IDataFrameAnalyzer = dependencies.analyzer
        self._logger: ILogger = dependencies.logger
        self._rich: IRichPrinter = dependencies.printer
        self._car_dataset: DataFrame = self._loader.get_car_dataset()

    def _show_main_options(self) -> None:
        """Display an interactive menu for the user to choose one of the options."""
        self._rich.print_rich(Rule(style="cyan"))
        self._rich.print_rich(Rule("NEXT ACTION", style="cyan"))
        self._rich.print_rich(Rule(style="cyan"))
        self._rich.print_panel("Main Menu", title="MENU", color="cyan")

        menu_table: Table = self._rich.create_table("Option", "Description")
        menu_table.add_row("1", "Analyze dataset")
        menu_table.add_row("2", "Clean dataset")
        menu_table.add_row("3", "Clear terminal")
        menu_table.add_row("4", "Exit program")
        self._rich.print_table(menu_table)

    @error_handler
    def display_main_menu(self) -> None:
        """Display menu for the user to choose options and then execute the proper
        logic according to the option selected.
        """
        while True:
            self._show_main_options()
            choice: str = input("\nEnter your choice:\n").strip()

            if choice == "1":
                self._analyzer.run_analyzer_menu(self._car_dataset)
            elif choice == "2":
                pass
            elif choice == "3":
                system("cls" if os_name == "nt" else "clear")
            elif choice == "4":
                self._rich.print_panel(
                    "Exiting program...", title="EXIT", color="green"
                )
                break
            else:
                self._rich.print_panel(
                    f"Option {choice} is invalid. Try again.",
                    title="ERROR",
                    color="red",
                )
