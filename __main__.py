import logging
from linear_regression.parser import Parser
from linear_regression.model import Model
from linear_regression.render import Render


def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    cars = Parser('data.csv').parse_cars()

    # intercept, slope = Parser('model.csv').parse_model()

    # model = Model(intercept=intercept, slope=slope)
    # price = model.estimate_price(cars[0])

    # print(f'Estimated price: {price}')
    # print(f'Actual price: {cars[0].price}')

    model = Model(cars=cars)
    model.train()

    Render(cars, model.intercept, model.slope)()

if __name__ == '__main__':
    main()
