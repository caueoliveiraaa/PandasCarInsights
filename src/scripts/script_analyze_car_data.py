"""
This script is responsible for reading data from 'database.dataset.json', cleaning
the data acquired, organazing and viewing it by applying data analysis techniques to
get insights about the car data.
"""

from beartype import beartype
from pandas import DataFrame, read_json

from configs.config import PATH_DATASET


@beartype
def get_dataset_into_dataframe() -> DataFrame:
    """
    Reads the data from 'database.dataset.json' and turns it into a DataFrame.

    Returns:
        DataFrame: Json dataset converted into a DataFrame.

    Raises:
        OSError: In case an error occurs when handling the json file.
        ValueError: In case there is a problem with the value in the json.
        TypeError: In case the json contains unexpected types.
    """
    dataset: DataFrame = DataFrame()

    try:
        dataset = read_json(PATH_DATASET)
        print("Extracted dataset:\n")
        print(dataset.head())
        print("\nDataset Information:\n")
        print(dataset.info())

    except OSError as e:
        raise OSError("Error reading the content of dataset.json.") from e
    except ValueError as e:
        raise ValueError("Expected object or value.") from e
    except TypeError as e:
        raise TypeError("JSON contains unexpected types.") from e

    return dataset


@beartype
def analyze_car_data() -> None:
    """
    Entry point of the script that executes the data analysis.
    """
    get_dataset_into_dataframe()


if __name__ == "__main__":
    analyze_car_data()
