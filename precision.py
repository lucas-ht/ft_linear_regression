import logging
from typing import List
from linear_regression.car import Car
from linear_regression.parser import Parser, DATA_FILE, MODEL_FILE
from linear_regression.model import Model
from linear_regression.render import Render

def get_cars() -> List[Car] | None:
    try:
        cars = Parser(DATA_FILE).parse_cars()
        return cars

    except Exception:
        return None

def get_model(cars: List[Car]) -> Model | None:
    try:
        intercept, slope = Parser(MODEL_FILE).parse_model()

        model = Model(cars=cars, intercept=intercept, slope=slope)
        return model

    except Exception:
        return None

def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    cars = get_cars()
    if cars is None:
        return

    model = get_model(cars)
    if model is None:
        return

    rmse = model.calculate_rmse()
    print(f'The Root Mean Squared Error (RMSE) of the model is {rmse:.2f}.')
    print('The RMSE indicates the precision of the model. The lower the RMSE, the better the model.')

if __name__ == '__main__':
    main()
