import logging
from typing import List
from .parser import Parser
from .car import Car

LEARNING_RATE   = 0.02
EPOCHS          = 50000

class Model:
    intercept:   float = 0.00
    slope:       float = 0.00

    min_mileage: float | None = None
    max_mileage: float | None = None
    min_price:   float | None = None
    max_price:   float | None = None

    def __init__(self, cars: List[Car] | None = None, intercept: float | None = None, slope: float | None = None) -> None:
        """
        Initialize the model with the given cars and parameters.
        """
        if cars is not None:
            self._initialize_cars(cars)

        if intercept is not None:
            self.intercept = intercept

        if slope is not None:
            self.slope = slope

    def estimate_price(self, car: Car) -> float:
        """
        Estimate the price of a car given its mileage.
        """
        return self.intercept + self.slope * car.mileage

    def train(self, learning_rate: float = LEARNING_RATE, epochs: float = EPOCHS) -> None:
        """
        Train the model using gradient descent.
        """
        for epoch in range(epochs):
            total_loss      = 0
            total_gradient  = 0

            for car in self.cars:
                estimated_price = self.estimate_price(car)
                total_loss      += estimated_price - car.price
                total_gradient  += (estimated_price - car.price) * car.mileage

            self.intercept  -= learning_rate * (total_loss / len(self.cars))
            self.slope      -= learning_rate * (total_gradient / len(self.cars))

            logging.debug(f'Epoch: {epoch}, intercept: {self.intercept}, slope: {self.slope}')

        logging.info(f'Finished Training after {EPOCHS} epochs with intercept: {self.intercept}, slope: {self.slope}')
        self._destandardize()
        Parser('model.csv').save_model(intercept=self.intercept, slope=self.slope)

    def _initialize_cars(self, cars: List[Car]) -> None:
        if not cars:
            raise ValueError("List of cars cannot be empty.")

        self.cars = cars

        mileages = [car.mileage for car in self.cars]
        self.min_mileage = min(mileages)
        self.max_mileage = max(mileages)

        prices = [car.price for car in self.cars]
        self.min_price = min(prices)
        self.max_price = max(prices)

        self._standardize()

    def _standardize(self) -> None:
        for car in self.cars:
            car.standardize(self.min_mileage, self.max_mileage, self.min_price, self.max_price)

        logging.debug(f'Standardized Data: min_mileage: {self.min_mileage}, max_mileage: {self.max_mileage}, min_price: {self.min_price}, max_price: {self.max_price}')

    def _destandardize(self) -> None:
        self.slope = self.slope * (self.max_price - self.min_price) / (self.max_mileage - self.min_mileage)
        self.intercept = self.intercept * (self.max_price - self.min_price) + self.min_price - self.slope * self.min_mileage

        for car in self.cars:
            car.destandardize(self.min_mileage, self.max_mileage, self.min_price, self.max_price)

        logging.debug(f'De-standardized Data: intercept: {self.intercept}, slope: {self.slope}')
