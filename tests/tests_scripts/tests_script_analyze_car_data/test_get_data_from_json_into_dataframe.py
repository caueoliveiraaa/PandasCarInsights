"""This file tests the method 'get_dataset_into_dataframe'."""

import unittest
from unittest.mock import MagicMock, patch

from beartype.typing import Any, List
from pandas import DataFrame

from src.scripts.script_analyze_car_data import get_dataset_into_dataframe
from tests.base_tests.base_test_case import BaseTestCase


class TestGetDatasetIntoDataframe(BaseTestCase):
    """Tests for the 'get_dataset_into_dataframe' method."""

    @patch("src.scripts.script_analyze_car_data.read_json")
    def test_valid_json(self, mock_read_json: MagicMock) -> None:
        """Test that valid JSON data is correctly converted to a DataFrame."""
        mock_read_json.return_value = DataFrame(self.mock_dataset)

        result: DataFrame = get_dataset_into_dataframe()

        self.assertIsInstance(result, DataFrame)
        self.assertTrue(len(result))
        self.assertTrue(result["Brand"][0], "Ford")
        self.assertTrue(result["Model"][0], "Fiesta")
        self.assertTrue(result["Year"][0], "2018")
        self.assertTrue(result["Horsepower"][0], "120")
        self.assertTrue(result["MPG"][0], "35")
        self.assertTrue(result["Color"][0], "Blue")

    @patch("src.scripts.script_analyze_car_data.read_json")
    def test_raise_exceptions(self, mock_read_json: MagicMock) -> None:
        """Test the raise of all the exceptions."""
        exceptions: List[Any] = [OSError, ValueError, TypeError]

        for exception in exceptions:
            result: DataFrame = DataFrame()
            with self.assertRaises(exception) as context:
                mock_read_json.side_effect = exception()
                result = get_dataset_into_dataframe()

            self.assertIsInstance(result, DataFrame)
            self.assertTrue(result.empty)
            validation: bool = (
                bool(
                    "Error reading the content of dataset.json."
                    in str(context.exception)
                )
                or bool("Expected object or value." in str(context.exception))
                or bool("JSON contains unexpected types." in str(context.exception))
            )
            self.assertTrue(validation)


if __name__ == "__main__":
    unittest.main()
