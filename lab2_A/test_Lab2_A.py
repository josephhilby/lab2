import io
import unittest
from unittest import mock

from lab2_A.jmh_Lab2_A import Triangle, main

class LabTwoATests(unittest.TestCase):
    def setUp(self):
        self.triangle = Triangle(10, 10, 10)

    def test_triangle_instance(self):
        isinstance(self.triangle, Triangle)

    def test_triangle_state(self):
        assert self.triangle.a == 10
        assert self.triangle.b == 10
        assert self.triangle.c == 10

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_triangle_behavior(self, mock_stdout):
        num_equal_sides = 2
        expected_output = "This is an equilateral triangle!\n"

        self.triangle.find_type()
        output = mock_stdout.getvalue()

        assert num_equal_sides == self.triangle.num_equal_sides()
        assert output == expected_output

    @unittest.mock.patch('builtins.input', side_effect=[10, 10, 10])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_main_one(self, mock_stdout, mock_input):
        main()
        assert mock_stdout.getvalue() == "This is an equilateral triangle!\n"

    @unittest.mock.patch('builtins.input', side_effect=[20, 20, 20.1])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_main_two(self, mock_stdout, mock_input):
        main()
        assert mock_stdout.getvalue() == "This is an isosceles triangle!\n"

    @unittest.mock.patch('builtins.input', side_effect=[1, 2, 3])
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_main_three(self, mock_stdout, mock_input):
        main()
        assert mock_stdout.getvalue() == "This is a scalene triangle!\n"