import task2
from unittest import TestCase


class TestTask2(TestCase):

    def setUp(self):
        """Init"""

    def test_task2(self):
        """Test for task2"""
        self.assertTrue(task2.is_leap_year(2000))
        self.assertTrue(task2.is_leap_year(2400))
        self.assertFalse(task2.is_leap_year(1900))
        self.assertFalse(task2.is_leap_year(10**6))

    def test_is_bool(self):
        """Test for task2"""
        self.assertTrue(type(task2.is_leap_year(1111)) == bool)

    def test_is_int(self):
        """Test for task2"""
        self.assertFalse(int(task2.is_leap_year(777)) is False)

    def tearDown(self):
        """Finish"""
