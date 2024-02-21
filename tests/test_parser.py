import logging
import unittest
from unittest.mock import patch, mock_open
from linear_regression.parser import Parser

def setUpModule():
    logging.basicConfig(
        level=logging.DEBUG,
        format='\n\033[1m%(levelname)-8s\033[0m %(message)s'
    )


class TestParser(unittest.TestCase):
    def setUp(self):
        self.parser = Parser('test.csv')

    @patch('builtins.open', new_callable=mock_open, read_data='intercept,slope\n1.0,2.0\n')
    def test_parse_model(self, mock_file):
        intercept, slope = self.parser.parse_model()
        self.assertEqual(intercept, 1.0)
        self.assertEqual(slope, 2.0)

    @patch('builtins.open', new_callable=mock_open)
    def test_save_model(self, mock_file):
        self.parser.save_model(1.0, 2.0)
        mock_file.assert_called_once_with('test.csv', 'w')

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_parse_model_not_found(self, mock_file):
        self.assertEqual(self.parser.parse_model(), (None, None))

    @patch('builtins.open', side_effect=PermissionError)
    def test_parse_model_permission_error(self, mock_file):
        self.assertEqual(self.parser.parse_model(), (None, None))

    @patch('builtins.open', new_callable=mock_open, read_data='mileage,price\n10000,20000\n20000,18000\n-1,1000\n,\n')
    def test_parse_cars(self, mock_file):
        cars = self.parser.parse_cars()
        self.assertEqual(len(cars), 2)
        self.assertEqual(cars[0].mileage, 10000)
        self.assertEqual(cars[0].price, 20000)
        self.assertEqual(cars[1].mileage, 20000)
        self.assertEqual(cars[1].price, 18000)

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_parse_cars_not_found(self, mock_file):
        self.assertEqual(self.parser.parse_cars(), None)

    @patch('builtins.open', side_effect=PermissionError)
    def test_parse_cars_permission_error(self, mock_file):
        self.assertEqual(self.parser.parse_cars(), None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
