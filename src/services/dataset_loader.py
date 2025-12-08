"""This module is responsible for storing the class that carries the logic
to extract and validate data being extracted from data sets.
"""

from beartype import beartype
from pandas import DataFrame, read_json

from config.config import PATH_CAR_DATASET
from src.interfaces.dataset_loader_interface import IDataSetLoader
from src.shared.error_handling import error_handler


class DataSetLoaderFactory(IDataSetLoader):
    """Class responsible for loading data sets."""

    def __init__(self) -> None:
        """Initialize data loader.

        Attributes:
            - self._path_car_dataset: Path to the car dataset.
            - self._car_dataset: The content of the dataset.
        """
        self._path_car_dataset: str = PATH_CAR_DATASET
        self._car_dataset: DataFrame = DataFrame()

    def load_car_dataset(self) -> None:
        """Read the data from 'car_dataset.json' and turn it into a DataFrame.

        Raises:
            ValueError: If there is a problem with the value in the json.
        """
        self._car_dataset = read_json(self._path_car_dataset)
        if not len(self._car_dataset):
            raise ValueError("Dataset cannot be empty.")

    @beartype
    @error_handler
    def get_car_dataset(self) -> DataFrame:
        """Load the dataset and return the content loaded.

        Returns:
            DataFrame: Data extracted from the dataset.
        """
        self.load_car_dataset()

        return self._car_dataset
