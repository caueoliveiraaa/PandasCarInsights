""" """

from src.interfaces.services.dataframe_cleaner_interface import IDataFrameCleaner
from src.interfaces.shared.rich_printer_interface import IRichPrinter


class DataFrameCleanerFactory(IDataFrameCleaner):
    """ """

    def __init__(self, printer: IRichPrinter) -> None:
        self._printer = printer
