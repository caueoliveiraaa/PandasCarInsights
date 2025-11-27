"""This file tests the method 'analyze_car_data'."""

import unittest
from unittest.mock import MagicMock, patch

from scripts.script_analyze_car_data import analyze_car_data
from tests.base_tests.base_test_case import BaseTestCase


class TestAnalyzeCarData(BaseTestCase):
    """Tests for the 'analyze_car_data' method."""

    @patch("scripts.script_analyze_car_data.get_dataset_into_dataframe")
    def test_execution_of_get_dataset_into_dataframe(
        self, mock_get_dataset_into_dataframe: MagicMock
    ) -> None:
        """Test that valid JSON data is correctly converted to a DataFrame."""
        mock_get_dataset_into_dataframe.side_effect = None

        self.assertIsNone(analyze_car_data())
        self.assertTrue(mock_get_dataset_into_dataframe.call_count == 1)


if __name__ == "__main__":
    unittest.main()
