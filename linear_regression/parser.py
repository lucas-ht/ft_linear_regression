import csv
from typing import List
from car import Car

class parser:
    def __init__(self, file: str) -> None:
        self.file = file

    def parse(self) -> List[Car]:
        cars = []

        with open(self.file, 'r') as file:
            reader = csv.reader(file)

            # Skip the header
            next(reader)

            for row in reader:
                car = Car(int(row[0]), int(row[1]))
                cars.append(car)

        return cars
