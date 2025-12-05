""" """

from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    model: str
    year: int
    horsepower: float | None
    mpg: float | None
    color: str | None
