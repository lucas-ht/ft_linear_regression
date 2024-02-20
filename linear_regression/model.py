import logging
from typing import List
from .car import Car

LEARNING_RATE   = 0.01
EPOCHS          = 50000

class Model:
    c: float    = +1.00
    m: float    = -1.00

    def __init__(self, cars: List[Car] | None = None, c: float | None = None, m: float | None = None) -> None:
        """
        Initialize the model with the given cars and parameters.
        """
        if cars is not None:
            self.cars = cars.copy()
            self._standardize()

        if c is not None:
            self.c = c

        if m is not None:
            self.m = m

    def estimate_price(self, car: Car) -> float:
        """
        Estimate the price of a car given its mileage.
        """
        return self.c + self.m * car.mileage

    def train(self, learning_rate: float = LEARNING_RATE, epochs: float = EPOCHS) -> None:
        """
        Train the model using gradient descent.
        """
        for epoch in range(epochs):
            l = 0
            g = 0

            for car in self.cars:
                estimated_price = self.estimate_price(car)
                l += (estimated_price - car.price)
                g += (estimated_price - car.price) * car.mileage

            self.c -= learning_rate * (l / len(self.cars))
            self.m -= learning_rate * (g / len(self.cars))

            logging.debug(f'Epoch: {epoch}, c: {self.c}, m: {self.m}')

        logging.info(f'Finished Training after {EPOCHS} epochs with c: {self.c} and m: {self.m}')
        self._destandardize()

    def _standardize(self) -> None:
        mileages = [car.mileage for car in self.cars]
        self.min_mileage = min(mileages)
        self.max_mileage = max(mileages)

        prices = [car.price for car in self.cars]
        self.min_price = min(prices)
        self.max_price = max(prices)

        for car in self.cars:
            car.standardize(self.min_mileage, self.max_mileage, self.min_price, self.max_price)

        logging.debug(f'Standardized Data: min_mileage: {self.min_mileage}, max_mileage: {self.max_mileage}, min_price: {self.min_price}, max_price: {self.max_price}')

    def _destandardize(self) -> None:
        self.m = self.m * (self.max_price - self.min_price) / (self.max_mileage - self.min_mileage)
        self.c = self.c * (self.max_price - self.min_price) + self.min_price - self.m * self.min_mileage

        for car in self.cars:
            car.destandardize(self.min_mileage, self.max_mileage, self.min_price, self.max_price)

        logging.debug(f'De-standardized Data: c: {self.c}, m: {self.m}')
