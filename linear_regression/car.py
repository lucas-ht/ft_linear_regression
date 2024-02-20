class Car:
    """
    A car with a mileage and a price.
    """
    mileage:             float
    price:               float

    def __init__(self, mileage: float, price: float) -> None:
        """
        Initialize the car with the given mileage and price.
        """
        self.mileage = mileage
        self.price   = price

    def standardize(self, min_mileage: float, max_mileage: float, min_price: float, max_price: float) -> None:
        """
        Standardize the mileage and price of the car to be between 0 and 1.
        """
        self.mileage = (self.mileage - min_mileage) / (max_mileage - min_mileage)
        self.price   = (self.price - min_price) / (max_price - min_price)

    def destandardize(self, min_mileage: float, max_mileage: float, min_price: float, max_price: float) -> None:
        """
        Destandardize the mileage and price of the car to be between the given minimum and maximum values.
        """
        self.mileage = self.mileage * (max_mileage - min_mileage) + min_mileage
        self.price = self.price * (max_price - min_price) + min_price

    def __str__(self) -> str:
        return f'Mileage: {self.mileage}, Price: {self.price}'
