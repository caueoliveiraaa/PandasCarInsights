"""This file stores relevant information shared among modules."""

import os

PATH_ROOT: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_DATASET: str = os.path.join(PATH_ROOT, "src\\data\\raw\\dataset.json")
PATH_LOGS: str = os.path.join(PATH_ROOT, "logs\\")
