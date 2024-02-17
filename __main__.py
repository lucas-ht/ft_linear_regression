from linear_regression.parser import parser
from linear_regression.render import render


def main() -> None:
    cars = parser('data.csv').parse()
    render(cars, 0, 0)()

if __name__ == '__main__':
    main()
