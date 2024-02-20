import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import logging
from typing import List
from .car import Car

logging.getLogger('matplotlib').setLevel(logging.WARNING)

class Render:
    CAR_COLOR        = 'blue'
    PREDICTION_COLOR = 'red'

    def __init__(self, cars: List[Car], intercept: float, slope: float) -> None:
        """
        Initialize the renderer with the given cars and parameters.
        """
        if not cars:
            raise ValueError("List of cars cannot be empty.")

        self.cars      = cars
        self.intercept = intercept
        self.slope     = slope

    def __call__(self) -> None:
        """
        Render the cars and the linear regression prediction.
        """
        plt.figure("ft_linear_regression")
        plt.xlabel('Mileage')
        plt.ylabel('Price')

        formatter = FuncFormatter(lambda x, _: '{:,.0f}'.format(x))
        plt.gca().xaxis.set_major_formatter(formatter)
        plt.gca().yaxis.set_major_formatter(formatter)

        self._render_cars()
        self._render_prediction()

        logging.info('Rendering the plot.')
        try:
            plt.show()
        except KeyboardInterrupt:
            pass
        except Exception:
            logging.error('Could not render the plot.', exc_info=True)

    def _render_cars(self) -> None:
        x = [car.mileage for car in self.cars]
        y = [car.price for car in self.cars]

        plt.scatter(x, y, color=self.CAR_COLOR)

    def _render_prediction(self) -> None:
        x_min = min([car.mileage for car in self.cars])
        x_max = max([car.mileage for car in self.cars])

        y_min = self.intercept + self.slope * x_min
        y_max = self.intercept + self.slope * x_max

        plt.plot([x_min, x_max], [y_min, y_max], color=self.PREDICTION_COLOR)
