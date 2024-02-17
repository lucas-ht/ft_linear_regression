class Car:
    def __init__(self, price: int, mileage: int):
        self.price   = price
        self.mileage = mileage

    def __str__(self):
        return f'Mileage: {self.mileage}, Price: {self.price}'
