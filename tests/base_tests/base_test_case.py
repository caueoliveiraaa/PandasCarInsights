"""File responsible for creating the base test class."""

import io
import sys
from unittest import TestCase
from unittest.mock import patch

import pandas as pd
from beartype.typing import Any, Dict, List, Union


class BaseTestCase(TestCase):
    """
    Base test class that sets up standard methods that can be imported
    by test classes to use the same methods.

    Thus, by simply importing the BaseTestCase, the "setUpClass"
    and "tearDownClass" methods below will be executed automatically, and elements
    like 'sleep' and 'print' will not affect the tests.
    """

    _patchers: Dict[str, Any] = {}
    _mocks: Dict[str, Any] = {}
    _original_stderr: Any = None

    def setUp(self) -> None:
        """
        Stores attributes, variables and constants that are shared across tests.

        Attributes:
            self.mock_dataset: Mocks the data in the dataset.
        """
        super().setUp()
        self.mock_dataset: List[Dict[str, Union[str, int]]] = [
            {
                "Brand": "Ford",
                "Model": "Fiesta",
                "Year": 2018,
                "Horsepower": 120,
                "MPG": 35,
                "Color": "Blue",
            },
            {
                "Brand": "Ford",
                "Model": "Focus",
                "Year": 2019,
                "Horsepower": 150,
                "MPG": None,
                "Color": "Red",
            },
            {
                "Brand": "Toyota",
                "Model": "Corolla",
                "Year": 2020,
                "Horsepower": 132,
                "MPG": 32,
                "Color": "White",
            },
            {
                "Brand": "Toyota",
                "Model": "Camry",
                "Year": 2018,
                "Horsepower": None,
                "MPG": 29,
                "Color": "Black",
            },
            {
                "Brand": "Honda",
                "Model": "Civic",
                "Year": 2021,
                "Horsepower": 158,
                "MPG": 36,
                "Color": "Silver",
            },
        ]

    @classmethod
    def setUpClass(cls) -> None:
        """
        Overrides methods that can influence tests when executing them.
        More methods to be overridden can be added here.

        Args:
            cls: It is a convention (like self), short for 'class'
        """
        cls._patchers = {
            "print": patch("builtins.print", return_value=None),
            "traceback": patch("traceback.print_exception", return_value=None),
            "sleep": patch("time.sleep", return_value=None),
            "logger": patch("logging.Logger._log", return_value=None),
            "df_head": patch.object(pd.DataFrame, "head", return_value=pd.DataFrame()),
            "df_tail": patch.object(pd.DataFrame, "tail", return_value=pd.DataFrame()),
            "df_info": patch.object(pd.DataFrame, "info", return_value=None),
        }

        cls._mocks = {name: patcher.start() for name, patcher in cls._patchers.items()}

        cls._original_stderr = sys.stderr
        sys.stderr = io.StringIO()

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Ends the methods that were overwritten at the end of the tests.
        More methods to be overridden can be added here.

        Args:
            cls: It is a convention (like self), short for 'class'
        """
        for patcher in cls._patchers.values():
            patcher.stop()

        sys.stderr = cls._original_stderr
