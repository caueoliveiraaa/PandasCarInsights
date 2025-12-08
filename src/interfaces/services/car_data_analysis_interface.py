"""This module stores the Interface for the car data analysis class."""

from abc import ABC, abstractmethod


class ICarDataAnalysis(ABC):
    """Interface for a datafrma analyzer class.

    This class is responsible for performing analysis operations on
    pandas DataFrames. It leverages a logger for recording analysis
    steps and a rich printer for styled console output.
    """

    @abstractmethod
    def _show_main_options(self) -> None:
        """Display an interactive menu for the user to choose one of the options."""
        pass

    @abstractmethod
    def display_main_menu(self) -> None:
        """Display menu for the user to choose options and then execute the proper
        logic according to the option selected.
        """
        pass
