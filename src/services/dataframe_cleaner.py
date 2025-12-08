""" """

from src.interfaces.dataframe_cleaner_interface import IDataFrameCleaner
from src.interfaces.rich_printer_interface import IRichPrinter


class DataFrameCleanerFactory(IDataFrameCleaner):
    """ """

    def __init__(self, printer: IRichPrinter) -> None:
        self._printer = printer
