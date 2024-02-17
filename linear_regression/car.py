class Car:
    def __init__(self, mileage: int, price: int):
        self.mileage = mileage
        self.price   = price

    def __str__(self):
        return f'Mileage: {self.mileage}, Price: {self.price}'
