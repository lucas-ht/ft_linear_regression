class Car:
    mileage:             float
    price:               float

    def __init__(self, mileage: float, price: float) -> None:
        self.mileage = mileage
        self.price   = price

    def standardize(self, min_mileage: float, max_mileage: float, min_price: float, max_price: float) -> None:
        self.mileage = (self.mileage - min_mileage) / (max_mileage - min_mileage)
        self.price   = (self.price - min_price) / (max_price - min_price)

    def destandardize(self, min_mileage: float, max_mileage: float, min_price: float, max_price: float) -> None:
        self.mileage = self.mileage * (max_mileage - min_mileage) + min_mileage
        self.price = self.price * (max_price - min_price) + min_price

    def __str__(self) -> str:
        return f'Mileage: {self.mileage}, Price: {self.price}'
