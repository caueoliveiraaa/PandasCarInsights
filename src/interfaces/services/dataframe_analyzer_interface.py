"""This module stores the Interface for dataframe analysis."""

from abc import ABC, abstractmethod

from pandas import DataFrame


class IDataFrameAnalyzer(ABC):
    """Interface for a datafrma analyzer class.

    This class is responsible for performing analysis operations on
    pandas DataFrames. It leverages a logger for recording analysis
    steps and a rich printer for styled console output.
    """

    @abstractmethod
    def _display_dataframe_information(self, df: DataFrame) -> None:
        """
        Display information about the dataset in an informative way.

        Args:
            df (DataFrame): Instance of DataFrame to print its information.
        """
        pass

    @abstractmethod
    def _show_column_data(self, df: DataFrame) -> None:
        """Display the dataset column names and their data types.

        Args:
            df (DataFrame): Instance of DataFrame with data from dataset.
        """
        pass

    @abstractmethod
    def _show_full_dataset(self, df: DataFrame) -> None:
        """Display the full dataset.

        Args:
            df (DataFrame): Instance of DataFrame with data from dataset.
        """
        pass

    @abstractmethod
    def _show_analyzer_options(self) -> None:
        """Display an interactive menu for the user to choose analysis options."""
        pass

    @abstractmethod
    def run_analyzer_menu(self, df: DataFrame) -> None:
        """Display menu for the user to choose any of the analysis options and then
        execute the proper logic according to the option selected.

        Args:
            df (DataFrame): Instance of DataFrame with data from dataset.
        """
        pass
