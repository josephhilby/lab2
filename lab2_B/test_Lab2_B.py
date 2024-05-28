import io
import unittest
from unittest import mock

from lab2_B.jmh_Lab2_B import FederalTax, federal_tax_data, main


class LabTwoBTests(unittest.TestCase):
    def setUp(self):
        self.tax = FederalTax(federal_tax_data)

    def test_tax_instance(self):
        isinstance(self.tax, FederalTax)

    def test_tax_state(self):
        assert self.tax.federal_tax_rates == federal_tax_data

    @unittest.mock.patch('builtins.input', return_value='1000000')
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_main_one(self, mock_stdout, mock_input):
        main()
        assert mock_stdout.getvalue() == "You owe $330332.00 this year.\n"

    @unittest.mock.patch('builtins.input', return_value='500000')
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_main_two(self, mock_stdout, mock_input):
        main()
        assert mock_stdout.getvalue() == "You owe $146894.50 this year.\n"

    @unittest.mock.patch('builtins.input', return_value='10.50')
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_main_three(self, mock_stdout, mock_input):
        main()
        assert mock_stdout.getvalue() == "You owe $1.05 this year.\n"


if __name__ == '__main__':
    unittest.main()