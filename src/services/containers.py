"""Dependency injection container for CarDataAnalysis and its dependencies."""

from dependency_injector import containers, providers

from src.domain.car_data_analysis import CarAnalysisDependencies
from src.services.car_data_analysis import CarDataAnalysis
from src.services.dataframe_analyzer import DataFrameAnalyzerFactory
from src.services.dataframe_cleaner import DataFrameCleanerFactory
from src.services.dataset_loader import DataSetLoaderFactory
from src.shared.base_logger import ProjectLoggerSingleton
from src.shared.rich_printer import RichPrinterSingleton


class CarDataAnalysisContainer(containers.DeclarativeContainer):
    """Dependency injection container for the CarDataAnalysis workflow.

    This container wires together all required services and shared singletons
    for performing car dataset analysis. It manages the lifecycle of objects
    such as loggers, printers, and data processing services.

    Components:
        config: Configuration provider for external values.
        logger: Singleton logger instance used across the project for logging.
        printer: Singleton rich printer instance used for styled console output.
        loader: Factory that produces dataset loader instances for reading car data.
        cleaner: Factory that makes dataframe cleaner instances for preprocessing data.
        analyzer: Factory that makes dataframe analyzer instances for doing analysis.
        dependencies: Factory that bundles all dependencies into an
            `CarAnalysisDependencies` dataclass, simplifying dependency injection.
        car_data_analysis: Factory that produces the main orchestrator
            `CarDataAnalysis`, with all dependencies injected via the
            `CarAnalysisDependencies` bundle.
    """

    config: providers.Configuration = providers.Configuration()

    logger: providers.Singleton[ProjectLoggerSingleton] = providers.Singleton(
        ProjectLoggerSingleton
    )
    printer: providers.Singleton[RichPrinterSingleton] = providers.Singleton(
        RichPrinterSingleton
    )

    loader: providers.Factory[DataSetLoaderFactory] = providers.Factory(
        DataSetLoaderFactory
    )
    cleaner: providers.Factory[DataFrameCleanerFactory] = providers.Factory(
        DataFrameCleanerFactory,
        printer=printer,
    )
    analyzer: providers.Factory[DataFrameAnalyzerFactory] = providers.Factory(
        DataFrameAnalyzerFactory,
        printer=printer,
    )

    analysis_dependencies: providers.Factory[CarAnalysisDependencies] = (
        providers.Factory(
            CarAnalysisDependencies,
            loader=loader,
            cleaner=cleaner,
            analyzer=analyzer,
            logger=logger,
            printer=printer,
        )
    )

    car_data_analysis: providers.Factory[CarDataAnalysis] = providers.Factory(
        CarDataAnalysis,
        dependencies=analysis_dependencies,
    )
