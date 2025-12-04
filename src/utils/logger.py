"""Utilities for setting up a project-wide file-based logger."""

import os
from datetime import datetime
from logging import DEBUG, FileHandler, Formatter, Logger, getLogger

from beartype import beartype
from beartype.typing import Optional

from config.config import PATH_LOGS


class BaseLogger:
    """Create and configure a project-level Logger."""

    @beartype
    def __init__(self, name: str = __name__, path: str = PATH_LOGS) -> None:
        """Initialize the logger helper.

        Args:
            name: A name for the logging process.
            path: Path prefix for log files. The file name will append the
                current date and the `.log` extension.
        """
        self._name: str = name
        self._path: str = path
        self._logger: Optional[Logger] = None
        self._logger_formatter: str = (
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
        self._setup_logger()

    @beartype
    def _setup_logger(self) -> None:
        """ """
        date_str: str = datetime.now().date().strftime("%Y_%m_%d")
        file_name: str = str(__name__).replace(".", "_")
        full_path: str = f"{self._path}{file_name}{date_str}.log"
        os.makedirs(os.path.dirname(self._path), exist_ok=True)

        self._logger = getLogger(self._name)
        self._set_handlers(full_path)
        if not self._logger:
            raise ValueError("Could not set up logger properly.")

    @beartype
    def _set_handlers(self, full_path: str) -> None:
        """Attach a `FileHandler` to the logger, removing any old handlers.

        Args:
            full_path: Full path to the log file (including file name).
        """
        for handler in self._logger.handlers:
            self._logger.removeHandler(handler)

        if not self._logger.handlers:
            self._logger.setLevel(level=DEBUG)
            file_handler: FileHandler = FileHandler(full_path)
            formatter: Formatter = Formatter(self._logger_formatter)

            file_handler.setFormatter(formatter)
            self._logger.addHandler(file_handler)

    @beartype
    def get_logger(self) -> Logger:
        """Return instance of Logger for logging information.

        Returns:
            Logger: Instance of Logger.
        """
        if not self._logger:
            raise ValueError("Could not set up logger properly.")

        return self._logger
