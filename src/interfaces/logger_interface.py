"""This module stores the Interface for logger implementations."""

from abc import ABC, abstractmethod
from logging import Logger


class ILogger(ABC):
    """Interface for logger class.

    Defines the contract for setting up a logger, attaching handlers,
    and retrieving the logger instance.
    """

    @abstractmethod
    def _setup_logger(self) -> None:
        """Configure the logger instance."""
        pass

    @abstractmethod
    def _set_handlers(self, full_path: str) -> None:
        """Attach handlers to the logger."""
        pass

    @abstractmethod
    def get_logger(self) -> Logger:
        """Return the configured logger instance."""
        pass
