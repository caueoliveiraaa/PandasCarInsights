"""This file stores relevant information shared among modules."""

import os

PATH_ROOT: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_LOGS: str = os.path.join(PATH_ROOT, "logs\\")
PATH_CAR_DATASET: str = os.path.join(PATH_ROOT, "src\\data\\raw\\car_dataset.json")
