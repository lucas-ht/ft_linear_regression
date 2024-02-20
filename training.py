import logging
from typing import List
from linear_regression.car import Car
from linear_regression.parser import Parser, DATA_FILE
from linear_regression.model import Model
from linear_regression.render import Render

def get_cars() -> List[Car] | None:
    cars = Parser(DATA_FILE).parse_cars()
    return cars

def main() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format='\033[1m%(levelname)-8s\033[0m %(message)s'
    )

    cars = get_cars()
    if cars is None:
        return

    model = Model(cars=cars)
    model.train()

    Render(cars, model.intercept, model.slope)()

if __name__ == '__main__':
    main()
