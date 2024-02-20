class Car:
    mileage:             float
    price:               float
    standardize_mileage: float | None = None
    standardize_price:   float | None = None

    def __init__(self, mileage: int, price: int) -> None:
        self.mileage = mileage
        self.price   = price

    def standardize(self, min_mileage: int, max_mileage: int, min_price: int, max_price: int) -> None:
        self.mileage = (self.mileage - min_mileage) / (max_mileage - min_mileage)
        self.price   = (self.price - min_price) / (max_price - min_price)

    def destandardize(self, min_mileage, max_mileage, min_price, max_price):
        self.mileage = self.mileage * (max_mileage - min_mileage) + min_mileage
        self.price = self.price * (max_price - min_price) + min_price

    def __str__(self) -> str:
        return f'Mileage: {self.mileage}, Price: {self.price}'
