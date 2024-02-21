import logging
from math import sqrt
from typing import List
from .parser import Parser, MODEL_FILE
from .car import Car

LEARNING_RATE:    float        = 0.01
EPOCHS:           int          = 20000

class Model:
    """
    A linear regression model to estimate the price of a car given its mileage.
    """
    intercept:    float        = 0.00
    slope:        float        = 0.00

    _min_mileage: float | None = None
    _max_mileage: float | None = None
    _min_price:   float | None = None
    _max_price:   float | None = None

    def __init__(self, cars: List[Car] | None = None, intercept: float | None = None, slope: float | None = None) -> None:
        """
        Initialize the model with the given cars and parameters.
        """
        if cars is not None:
            self.cars = cars

        if intercept is not None:
            self.intercept = intercept

        if slope is not None:
            self.slope = slope

    def estimate_price(self, mileage: float) -> float:
        """
        Estimate the price of a car given its mileage.
        """
        return self.intercept + self.slope * mileage

    def train(self, learning_rate: float = LEARNING_RATE, epochs: float = EPOCHS) -> None:
        """
        Train the model using gradient descent.
        """
        self._standardize()
        logging.info(f'Training Model with learning_rate: {learning_rate}, epochs: {epochs}')

        for epoch in range(epochs):
            total_loss      = 0
            total_gradient  = 0

            for car in self.cars:
                estimated_price = self.estimate_price(car.mileage)
                total_loss      += estimated_price - car.price
                total_gradient  += (estimated_price - car.price) * car.mileage

            self.intercept  -= learning_rate * (total_loss / len(self.cars))
            self.slope      -= learning_rate * (total_gradient / len(self.cars))

            logging.debug(f'Epoch: {epoch}, intercept: {self.intercept}, slope: {self.slope}')

        logging.info(f'Finished Training after {EPOCHS} epochs with intercept: {self.intercept}, slope: {self.slope}')
        self._destandardize()

    def calculate_rmse(self) -> float:
        """
        Calculate the Root Mean Squared Error (RMSE) of the model.
        """
        total_squared_error = 0

        for car in self.cars:
            estimated_price = self.estimate_price(car.mileage)
            error = estimated_price - car.price
            total_squared_error += error ** 2

        mean_squared_error = total_squared_error / len(self.cars)
        root_mean_squared_error = sqrt(mean_squared_error)

        return root_mean_squared_error

    def _standardize(self) -> None:
        mileages = [car.mileage for car in self.cars]
        self._min_mileage = min(mileages)
        self._max_mileage = max(mileages)

        prices = [car.price for car in self.cars]
        self._min_price = min(prices)
        self._max_price = max(prices)

        for car in self.cars:
            car.standardize(self._min_mileage, self._max_mileage, self._min_price, self._max_price)

        logging.debug(f'Standardized Data: min_mileage: {self._min_mileage}, max_mileage: {self._max_mileage}, min_price: {self._min_price}, max_price: {self._max_price}')

    def _destandardize(self) -> None:
        self.slope = self.slope * (self._max_price - self._min_price) / (self._max_mileage - self._min_mileage)
        self.intercept = self.intercept * (self._max_price - self._min_price) + self._min_price - self.slope * self._min_mileage

        for car in self.cars:
            car.destandardize(self._min_mileage, self._max_mileage, self._min_price, self._max_price)

        logging.debug(f'De-standardized Data: intercept: {self.intercept}, slope: {self.slope}')
