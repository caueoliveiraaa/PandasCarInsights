"""Store dataclass that defines the classes being used by the
car data analysis logic.
"""

from dataclasses import dataclass

from src.interfaces.dataframe_analyzer_interface import IDataFrameAnalyzer
from src.interfaces.dataframe_cleaner_interface import IDataFrameCleaner
from src.interfaces.dataset_loader_interface import IDataSetLoader
from src.interfaces.logger_interface import ILogger
from src.interfaces.rich_printer_interface import IRichPrinter


@dataclass
class CarAnalysisDependencies:
    """Define interfaces of the classes being used for the car analysis.

    Attributes:
        loader: Class responsible for loading data sets.
        cleaner: Class responsible for cleaning dataframes.
        analyzer: Class responsible for analysing dataframes.
        logger: Class responsible for logging.
        printer: Class responsible for printing customized messages.
    """

    loader: IDataSetLoader
    cleaner: IDataFrameCleaner
    analyzer: IDataFrameAnalyzer
    logger: ILogger
    printer: IRichPrinter
