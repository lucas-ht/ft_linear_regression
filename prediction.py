import logging
from linear_regression.parser import Parser, MODEL_FILE
from linear_regression.model import Model

def get_mileage() -> float | None:
    try:
        mileage = input('Enter the mileage of the car: ')

        mileage = float(mileage)
        if mileage < 0:
            raise ValueError('mileage cannot be negative')

        return mileage

    except KeyboardInterrupt:
        return None
    except Exception as e:
        logging.error(f'Invalid mileage: {e}')
        return None

def get_model() -> Model | None:
    intercept, slope = Parser(MODEL_FILE).parse_model()
    if intercept is None or slope is None:
        return None

    model = Model(intercept=intercept, slope=slope)
    return model

def main() -> None:
    logging.basicConfig(
        level=logging.DEBUG,
        format='\033[1m%(levelname)-8s\033[0m %(message)s'
    )

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
