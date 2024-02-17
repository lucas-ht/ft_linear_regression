import matplotlib.pyplot as plt
from typing import List
from .car import Car

class render:
    def __init__(self, cars: List[Car], m: int, c: int) -> None:
        self.cars = cars
        self.m    = m
        self.c    = c

    def __call__(self) -> None:
        self._render_cars()
        self._render_prediction()

        plt.xlabel('Mileage')
        plt.ylabel('Price')
        plt.title('ft_linear_regression')

        plt.show()

    def _render_cars(self):
        x = [car.mileage for car in self.cars]
        y = [car.price for car in self.cars]

        plt.scatter(x, y, color='blue')

    def _render_prediction(self):
        x_min, x_max = 0, max([car.mileage for car in self.cars])

        y_min = self.m * x_min + self.c
        y_max = self.m * x_max + self.c

        plt.plot([x_min, x_max], [y_min, y_max], color='red')
