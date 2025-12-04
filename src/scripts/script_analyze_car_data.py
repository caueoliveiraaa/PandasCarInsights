"""This script is responsible for reading data from 'database.dataset.json', cleaning
the data acquired, organazing and viewing it by applying data analysis techniques to
get insights about the car data.
"""

from io import StringIO
from logging import Logger
from os import system

from beartype import beartype
from pandas import DataFrame, read_json
from rich.errors import ConsoleError, StyleError
from rich.rule import Rule
from rich.table import Table

from config.config import PATH_DATASET
from src.utils.printer import RichPrinter


class CarDataAnalysis:
    """Create logic for analyzing data from 'database.dataset.json'."""

    @beartype
    def __init__(self, logger: Logger, rich: RichPrinter) -> None:
        """Initialize the CarDataAnalysis for data analysis.
        Utilizes dependency injection for composition of objects.

        Attributes:
            logger: Instance of Logger for logging information.
        """
        self._path_dataset: str = PATH_DATASET
        self._dataset: DataFrame = DataFrame()
        self._logger: Logger = logger
        self._rich: RichPrinter = rich

    def set_dataset_into_dataframe(self) -> None:
        """Read the data from 'database.dataset.json' and turn it into a DataFrame.

        Raises:
            OSError: If an error occurs when handling the json file.
            ValueError: If there is a problem with the value in the json.
            TypeError: If the json contains unexpected types.
        """
        try:
            self._dataset = read_json(self._path_dataset)
            if not len(self._dataset):
                raise ValueError("Dataset cannot be empty.")
        except OSError as e:
            self._logger.error(e)
            raise OSError("Error reading the content of dataset.json.") from e
        except ValueError as e:
            self._logger.error(e)
            raise ValueError("Expected object or value.") from e
        except TypeError as e:
            self._logger.error(e)
            raise TypeError("JSON contains unexpected types.") from e

    def display_dataset_content_information(self) -> None:
        """Display information about the dataset in an informative way."""
        head_dataframe: DataFrame = self._dataset.head()
        self._rich.print_panel(
            "Dataset - method head() (5 first rows)", title="HEAD", color="cyan"
        )
        self._rich.display_dataframe_as_table(head_dataframe)

        tail_dataframe: DataFrame = self._dataset.tail()
        self._rich.print_panel(
            "Dataset - method tail() (5 last rows)", title="TAIL", color="cyan"
        )
        self._rich.display_dataframe_as_table(tail_dataframe)

        datafram_information = StringIO()
        self._dataset.info(buf=datafram_information)
        info_text = datafram_information.getvalue()
        self._rich.print_panel("Dataset - method info()", title="INFO", color="cyan")
        self._rich.print_panel(info_text)

    def show_basic_statistics(self) -> None:
        """Display basic statistical summary of the dataset."""
        stats_dataframe: DataFrame = self._dataset.describe()
        self._rich.print_panel(
            "Basic Statistics - method describe()", title="STATS", color="green"
        )
        self._rich.display_dataframe_as_table(stats_dataframe)

    def show_column_names(self) -> None:
        """Display the dataset column names."""
        table: Table = self._rich.create_table("Column Name")
        for col in self._dataset.columns:
            table.add_row(col)

        self._rich.print_panel("Dataset Columns", title="COLUMNS", color="cyan")
        self._rich.print_table(table)

    def show_full_dataset(self) -> None:
        """."""
        self._rich.print_panel("Complete Dataset", title="COLUMNS", color="cyan")
        self._rich.display_dataframe_as_table(self._dataset)

    def display_menu_with_options(self) -> None:
        """Display an interactive menu for the user to choose analysis options."""
        while True:
            self._rich.print_rich(Rule(style="cyan"))
            self._rich.print_rich(Rule("NEXT ACTION", style="cyan"))
            self._rich.print_rich(Rule(style="cyan"))
            self._rich.print_panel(
                "Pandas - Car Data Analysis Menu", title="MENU", color="cyan"
            )

            menu_table: Table = self._rich.create_table("Option", "Description")
            menu_table.add_row("1", "Show dataset head, tail and info")
            menu_table.add_row("2", "Show basic statistics")
            menu_table.add_row("3", "Show column names")
            menu_table.add_row("4", "Show full dataset")
            menu_table.add_row("5", "Clear terminal")
            menu_table.add_row("6", "Exit program")
            self._rich.print_table(menu_table)

            choice: str = input("\nEnter your choice: ").strip()
            self._rich.print_rich(Rule(style="cyan"))

            if choice == "1":
                self.display_dataset_content_information()
            elif choice == "2":
                self.show_basic_statistics()
            elif choice == "3":
                self.show_column_names()
            elif choice == "4":
                self.show_full_dataset()
            elif choice == "5":
                system("cls")
            elif choice == "6":
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

    def analyze_car_data(self) -> None:
        """Entry point of the script that executes the data analysis.

        Raises:
            OSError: If an error occurs when handling the json file.
            ValueError: If there is a problem with the value in the json.
            TypeError: If the json contains unexpected types.
            ConsoleError: If an error occurs in console operation.
            StyleError: If an error occurs when applying styles.
        """
        try:
            self.set_dataset_into_dataframe()
            self.display_menu_with_options()
        except OSError as e:
            self._logger.error(e)
            raise OSError("Error reading the content of dataset.json.") from e
        except ValueError as e:
            self._logger.error(e)
            raise ValueError("Expected object or value.") from e
        except TypeError as e:
            self._logger.error(e)
            raise TypeError("JSON contains unexpected types.") from e
        except ConsoleError as e:
            self._logger.error(e)
            raise ConsoleError("Error executing rich on terminal.") from e
        except StyleError as e:
            self._logger.error(e)
            raise StyleError("Error applying styles to the terminal.") from e
        except (KeyboardInterrupt, EOFError):
            exit()
