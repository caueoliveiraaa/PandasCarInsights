"""This file stores relevant information shared among modules."""

import os

PATH_ROOT: str = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PATH_DATASET: str = os.path.join(PATH_ROOT, "data\\raw\\dataset.json")
