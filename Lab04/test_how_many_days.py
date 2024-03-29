from unittest import TestCase
from Lab04 import time_calculator


class TestHow_many_days(TestCase):
    def test_how_many_days_lt_1(self):
        self.assertEqual(0, time_calculator.how_many_days(700))

    def test_how_many_days_eq_1(self):
        self.assertEqual(1, time_calculator.how_many_days(86400))

    def test_how_many_days_gt_1_lt_2(self):
        self.assertEqual(1, time_calculator.how_many_days(95000))

    def test_how_many_days_eq_2(self):
        self.assertEqual(2, time_calculator.how_many_days(172800))
