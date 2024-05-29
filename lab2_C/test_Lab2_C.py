import io
import unittest
from unittest import mock

from lab2_C.jmh_Lab2_C import Temperature, main


class LabOneATests(unittest.TestCase):
    def setUp(self):
        self.temp1 = Temperature(degree=-40.5, type="Fahrenheit")
        self.temp2 = Temperature(degree=20, type="Celsius")
        self.temp3 = Temperature(degree=350, type="Kelvin")

    def test_temperature_instance(self):
        isinstance(self.temp1, Temperature)

    def test_temperature_state(self):
        assert self.temp1.degree == -40.5
        assert self.temp2.degree == 20
        assert self.temp1.type == 'Fahrenheit'

    def test_temperature_behavior(self):
        self.temp1.convert_to_celsius()
        self.temp1.convert_from_celsius("Kelvin")

        self.temp2.convert_to_celsius()

        self.temp3.convert_to_celsius()
        self.temp3.convert_from_celsius("Fahrenheit")

        assert round(self.temp1.degree, 1) == 232.9 and self.temp1.type == "Kelvin"
        assert round(self.temp2.degree, 1) == 20.0 and self.temp2.type == "Celsius"
        assert round(self.temp3.degree, 1) == 170.3 and self.temp3.type == "Fahrenheit"

    @unittest.mock.patch('builtins.input', side_effect=["Fahrenheit", "Kelvin", -40.5])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_main_one(self, mock_stdout, mock_input):
        main()
        assert mock_stdout.getvalue() == "That is 232.9 degrees Kelvin.\n"

    @unittest.mock.patch('builtins.input', side_effect=["Celsius", "Celsius", 20.0])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_main_two(self, mock_stdout, mock_input):
        main()
        assert mock_stdout.getvalue() == "That is 20.0 degrees Celsius.\n"

    @unittest.mock.patch('builtins.input', side_effect=["Kelvin", "Fahrenheit", 350])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_main_three(self, mock_stdout, mock_input):
        main()
        assert mock_stdout.getvalue() == "That is 170.3 degrees Fahrenheit.\n"


if __name__ == '__main__':
    unittest.main()
