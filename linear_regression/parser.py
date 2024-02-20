import csv
import logging
from typing import List
from .car import Car

class Parser:
    def __init__(self, file: str) -> None:
        self.file = file

    def parse_cars(self) -> List[Car]:
        cars = []

        with open(self.file, 'r') as file:
            reader = csv.reader(file)

            # Skip the header
            next(reader)

            for row in reader:
                car = self._parse_car(row)
                if car is not None:
                    cars.append(car)

        return cars

    @staticmethod
    def _parse_car(row: List[str]) -> Car | None:
        try:
            mileage = int(row[0])
            price   = int(row[1])

            if mileage < 0 or price < 0:
                raise ValueError('value must be positive')

            return Car(mileage, price)

        except (IndexError, ValueError):
            logging.error(f'Invalid row: {row}.', exc_info=True)
            return None
