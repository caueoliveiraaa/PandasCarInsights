"""This module stores the Interface for loader implementations."""

from abc import ABC, abstractmethod

from pandas import DataFrame


class IDataSetLoader(ABC):
    """Interface for loader class.

    Defines the contract for setting up a data loader that extracts data
    from pre-defined datasets.
    """

    @abstractmethod
    def load_car_dataset(self) -> None:
        """Read the data from 'car_dataset.json' and turn it into a DataFrame.

        The path to the dataset is defined in the constructor.

        Raises:
            OSError: If an error occurs when handling the json file.
            ValueError: If there is a problem with the value in the json.
            TypeError: If the json contains unexpected types.
        """
        pass

    @abstractmethod
    def get_car_dataset(self) -> DataFrame:
        """Load the dataset and return the content loaded.

        Returns:
            DataFrame: Data extracted from the dataset.

        Raises:
            OSError: If an error occurs when handling the json file.
            ValueError: If there is a problem with the value in the json.
            TypeError: If the json contains unexpected types.
        """
        pass
