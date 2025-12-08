"""Store class for implenting logic that analyzes different dataframes."""

from io import StringIO

from beartype import beartype
from pandas import DataFrame
from rich.rule import Rule
from rich.table import Table

from src.interfaces.services.dataframe_analyzer_interface import IDataFrameAnalyzer
from src.interfaces.shared.rich_printer_interface import IRichPrinter


class DataFrameAnalyzerFactory(IDataFrameAnalyzer):
    """Concrete implementation of the dataframe analyzer interface.

    This class is responsible for performing analysis operations on
    pandas DataFrames. It leverages a logger for recording analysis
    steps and a rich printer for styled console output.
    """

    @beartype
    def __init__(self, printer: IRichPrinter) -> None:
        """Initialize the DataFrameAnalyzerFactory with its dependencies.

        Args:
            printer (IRichPrinter): Rich printer instance used to display
                styled messages and results in the console.

        Attributes:
            self._rich (IRichPrinter): Internal reference to the injected printer.
        """
        self._rich = printer

    @beartype
    def _display_dataframe_information(self, df: DataFrame) -> None:
        """
        Display information about the dataset in an informative way.

        Args:
            df (DataFrame): Instance of DataFrame to print its information.
        """
        head_dataframe: DataFrame = df.head()
        self._rich.print_panel(
            "Dataset - method head() (5 first rows)", title="HEAD", color="cyan"
        )
        self._rich.display_dataframe_as_table(head_dataframe)

        tail_dataframe: DataFrame = df.tail()
        self._rich.print_panel(
            "Dataset - method tail() (5 last rows)", title="TAIL", color="cyan"
        )
        self._rich.display_dataframe_as_table(tail_dataframe)

        datafram_information = StringIO()
        df.info(buf=datafram_information)
        info_text = datafram_information.getvalue()

        self._rich.print_panel("Dataset - method info()", title="INFO", color="cyan")
        self._rich.print_panel(info_text)

    @beartype
    def _show_column_data(self, df: DataFrame) -> None:
        """Display the dataset column names and their data types.

        Args:
            df (DataFrame): Instance of DataFrame with data from dataset.
        """
        table: Table = self._rich.create_table("Column Name", "Data Type")
        for col in df.columns:
            dtype = str(df[col].dtype)
            table.add_row(col, dtype)

        self._rich.print_panel("Dataset Columns", title="COLUMNS", color="cyan")
        self._rich.print_table(table)

    @beartype
    def _show_full_dataset(self, df: DataFrame) -> None:
        """Display the full dataset.

        Args:
            df (DataFrame): Instance of DataFrame with data from dataset.
        """
        self._rich.print_panel("Complete Dataset", title="DATASET", color="cyan")
        self._rich.display_dataframe_as_table(df)

    def _show_analyzer_options(self) -> None:
        """Display an interactive menu for the user to choose analysis options."""
        self._rich.print_rich(Rule(style="cyan"))
        self._rich.print_rich(Rule("NEXT ACTION", style="cyan"))
        self._rich.print_rich(Rule(style="cyan"))
        self._rich.print_panel(
            "Data Analysis Menu",
            title="MENU",
            color="deep_sky_blue1",
        )

        menu_table: Table = self._rich.create_table("Option", "Description")
        menu_table.add_row("1", "Show dataset - Information")
        menu_table.add_row("2", "Show dataset - Column names and types")
        menu_table.add_row("3", "Show dataset - Full dataset")
        menu_table.add_row("4", "Return to main menu")
        self._rich.print_table(menu_table)

    def run_analyzer_menu(self, df: DataFrame) -> None:
        """Display menu for the user to choose any of the analysis options and then
        execute the proper logic according to the option selected.

        Args:
            df (DataFrame): Instance of DataFrame with data from dataset.
        """
        while True:
            self._show_analyzer_options()
            choice: str = input("\nEnter your choice:\n").strip()
            self._rich.print_rich(Rule(style="cyan"))

            if choice == "1":
                self._display_dataframe_information(df)
            elif choice == "2":
                self._show_column_data(df)
            elif choice == "3":
                self._show_full_dataset(df)
            elif choice == "4":
                break
            else:
                self._rich.print_panel(
                    f"Option {choice} is invalid. Try again.",
                    title="ERROR",
                    color="red",
                )
