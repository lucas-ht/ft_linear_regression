import csv
import logging
from typing import List, Tuple
from .car import Car

class Parser:
    def __init__(self, file: str) -> None:
        self._file = file

    def save_model(self, intercept: float, slope: float) -> None:
        """
        Save the model to the file.
        """
        try:
            with open(self._file, 'w') as file:
                writer = csv.writer(file)

                writer.writerow(['intercept', 'slope'])
                writer.writerow([intercept, slope])

                logging.info(f'Saved model with intercept: {intercept}, slope: {slope} to `{self.file}`.')
        except (FileNotFoundError, IndexError, ValueError):
            logging.error('Could not save model.', exc_info=True)

    def parse_model(self) -> Tuple[float | None, float | None] | None:
        """
        Parse the model from the file.
        """
        try:
            with open(self._file, 'r') as file:
                reader = csv.reader(file)

                # Skip the header
                next(reader)

                row = next(reader)
                intercept, slope = float(row[0]), float(row[1])

                logging.info(f'Parsed model with intercept: {intercept}, slope: {slope}')
                return intercept, slope

        except (FileNotFoundError, IndexError, ValueError):
            logging.error('Could not parse model.', exc_info=True)
            return None

    def parse_cars(self) -> List[Car] | None:
        """
        Parse the cars from the file.
        """
        cars = []

        try:
            with open(self._file, 'r') as file:
                reader = csv.reader(file)

                # Skip the header
                next(reader)

                for row in reader:
                    car = self._parse_car(row)
                    if car is not None:
                        cars.append(car)

                logging.info(f'Parsed {len(cars)} cars.')
                return cars

        except (FileNotFoundError, ValueError, csv.Error):
            logging.error(f'Could not parse cars from file: `{self.file}`.', exc_info=True)
            return None

    @staticmethod
    def _parse_car(row: List[str]) -> Car | None:
        try:
            logging.debug(f'Parsing row: `{" ".join(row)}`.')
            mileage = int(row[0])
            price   = int(row[1])

            if mileage < 0 or price < 0:
                raise ValueError('value must be positive')

            return Car(mileage, price)

        except (IndexError, ValueError):
            logging.error(f"Invalid row: `{' '.join(row)}`.", exc_info=True)
