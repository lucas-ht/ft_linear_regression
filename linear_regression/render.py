import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import logging
from typing import List
from .car import Car

logging.getLogger('matplotlib').setLevel(logging.WARNING)

class Render:
    """
    A renderer to visualize the cars and the linear regression prediction.
    """
    CAR_COLOR               = '#B6CEFFFF'
    LINEAR_REGRESSION_COLOR = '#FFADADFF'

    def __init__(self, cars: List[Car], intercept: float, slope: float) -> None:
        """
        Initialize the renderer with the given cars and parameters.
        """
        self.cars      = cars
        self.intercept = intercept
        self.slope     = slope

    def __call__(self) -> None:
        """
        Render the cars and the linear regression prediction.
        """
        plt.figure('ft_linear_regression')
        plt.title('ft_linear_regression', fontsize=12, pad=12)
        plt.xlabel('Mileage', labelpad=12, fontsize=10)
        plt.ylabel('Price', labelpad=12, fontsize=10)
        plt.tick_params(labelsize=6)

        formatter = FuncFormatter(lambda x, _: '{:,.0f}'.format(x))
        plt.gca().xaxis.set_major_formatter(formatter)
        plt.gca().yaxis.set_major_formatter(formatter)

        self._render_cars()
        self._render_linear_regression()

        plt.legend()
        plt.tight_layout()

        logging.info('Rendering the plot.')
        try:
            plt.show()
        except KeyboardInterrupt:
            pass
        except Exception as e:
            logging.error(f'Could not render the plot: {e}', exc_info=False)

    def _render_cars(self) -> None:
        x = [car.mileage for car in self.cars]
        y = [car.price for car in self.cars]

        plt.scatter(x, y, label="Car", color=self.CAR_COLOR, s=50)

    def _render_linear_regression(self) -> None:
        x_min = min([car.mileage for car in self.cars])
        x_max = max([car.mileage for car in self.cars])

        y_min = self.intercept + self.slope * x_min
        y_max = self.intercept + self.slope * x_max

        plt.plot(
            [x_min, x_max], [y_min, y_max],
            label='Linear regression', color=self.LINEAR_REGRESSION_COLOR, linewidth=2
        )
