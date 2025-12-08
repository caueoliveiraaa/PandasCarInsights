"""Error handling decorator for consistent logging and styled console output."""

from functools import wraps
from typing import Callable

from beartype.typing import Any, Optional
from rich.errors import ConsoleError, StyleError


def error_handler(func: Callable[..., Any]) -> Callable[..., Optional[Any]]:
    """Decorator for instance methods that handles errors using self._logger and
    self._rich.

    This decorator assumes the decorated method belongs to a class that has
    `_logger` and `_rich` attributes. It centralizes error handling so you
    don't need to repeat try/except blocks in every method.
    """

    @wraps(func)
    def wrapper(self: Any, *args: Any, **kwargs: Any) -> Optional[Any]:
        """Execute the wrapped method with error handling.

        Args:
            self: The instance of the class (must have `_logger` and `_rich`).
            *args: Positional arguments for the wrapped method.
            **kwargs: Keyword arguments for the wrapped method.

        Returns:
            Any: The result of the wrapped method if successful,
            otherwise None if an error occurs.
        """
        try:
            return func(self, *args, **kwargs)

        except (OSError, ValueError, TypeError) as e:
            self._logger.error(f"[Operational Error] {func.__name__}: {e}")
            self._rich.print_panel(
                "An operational error occurred while processing your request.\n"
                "Please check the logs for more details.",
                title="ERROR",
                color="red",
            )
            return None

        except (ConsoleError, StyleError) as e:
            self._logger.error(f"[Rich Console Error] {func.__name__}: {e}")
            self._rich.print_panel(
                "A console rendering error occurred while using Rich.\n"
                "Please check the logs for technical details.",
                title="RICH ERROR",
                color="red",
            )
            return None

        except (KeyboardInterrupt, EOFError):
            self._rich.print_panel(
                "Program interrupted by user.\nExiting gracefully...",
                title="EXIT",
                color="yellow",
            )
            exit()

    return wrapper
