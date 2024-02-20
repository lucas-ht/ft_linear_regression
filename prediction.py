import logging
from linear_regression.parser import Parser, MODEL_FILE
from linear_regression.model import Model

def get_mileage() -> float | None:
    mileage = input('Enter the mileage of the car: ')
    try:
        mileage = float(mileage)
        if mileage < 0:
            raise ValueError('mileage cannot be negative')
        return mileage

    except ValueError:
        logging.error('Invalid mileage.', exc_info=True)
        return None

def get_model() -> Model | None:
    try:
        intercept, slope = Parser(MODEL_FILE).parse_model()

        model = Model(intercept=intercept, slope=slope)
        return model

    except Exception:
        return None

def main() -> None:
    logging.basicConfig(level=logging.DEBUG)

    model = get_model()
    if model is None:
        return

    mileage = get_mileage()
    if mileage is None:
        return

    price = model.estimate_price(mileage)
    if price < 0:
        price = 0

    print(f'Estimated price: {price:.2f}')

if __name__ == '__main__':
    main()
