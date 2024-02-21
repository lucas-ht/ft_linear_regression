import logging
import unittest
from linear_regression.model import Model
from linear_regression.car import Car

def setUpModule():
    logging.basicConfig(
        level=logging.DEBUG,
        format='\n\033[1m%(levelname)-8s\033[0m %(message)s'
    )


class TestModel(unittest.TestCase):
    def setUp(self):
        self.cars = [
            Car(mileage=10000, price=20000),
            Car(mileage=20000, price=40000),
            Car(mileage=30000, price=60000),
            Car(mileage=40000, price=80000),
            Car(mileage=50000, price=100000),
        ]
        self.model = Model(cars=self.cars)

    def test_estimate_price(self):
        self.model.intercept = 20000
        self.model.slope = -0.5
        estimated_price = self.model.estimate_price(10000)
        self.assertEqual(estimated_price, 15000)

    def test_train(self):
        self.model.train(learning_rate=0.5, epochs=200, should_save_model=False)

        # Check that the model parameters have been updated
        self.assertNotEqual(self.model.intercept, 0)
        self.assertNotEqual(self.model.slope, 0)

        for car in self.cars:
            estimated_price = self.model.estimate_price(car.mileage)
            logging.debug(f'Estimated price: {estimated_price}, actual price: {car.price}')
            self.assertAlmostEqual(estimated_price, car.price, delta=100)

    def test_calculate_rmse(self):
        self.model.intercept = 20000
        self.model.slope = -0.5
        rmse = self.model.calculate_rmse()
        self.assertGreater(rmse, 0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
