import logging
from typing import List
from linear_regression.car import Car
from linear_regression.parser import Parser, DATA_FILE, MODEL_FILE
from linear_regression.model import Model

def get_cars() -> List[Car] | None:
    cars = Parser(DATA_FILE).parse_cars()
    return cars

def save_model(intercept: float, slope: float) -> None:
    Parser(MODEL_FILE).save_model(intercept, slope)


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

    save_model(model.intercept, model.slope)

    print('The model has been trained successfully.')

if __name__ == '__main__':
    main()
