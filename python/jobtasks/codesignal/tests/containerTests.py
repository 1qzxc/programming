import inspect, os, sys
current_dir = os.path.dirname(os.path.abspath(
    inspect.getfile(inspect.currentframe())
))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from timeout_decorator import timeout
import unittest
from container import Container


class DemoICATest(unittest.TestCase):
    """
    This test class includes 10 tests.

    All have the same score.
    You are not allowed to modify this file,
    but feel free to read the source code
    to better understand the details of all test cases.
    """

    failureException = Exception

    @classmethod
    def setUp(cls):
        cls.container = Container()

    @timeout(0.1)
    def test_01_simpleGetOddLength(self):
        """
        Add 1, 2, 5, 7, 9 -> [1, 2, 5, 7, 9]
        Median of [1, 2, 5, 7, 9] is 5
        Add 3, 4 -> [1, 2, 3, 4, 5, 7, 9]
        Median of [1, 2, 3, 4, 5, 7, 9] is 4
        """
        self.container.add(1)
        self.container.add(2)
        self.container.add(5)
        self.container.add(7)
        self.container.add(9)
        self.assertEqual(self.container.get_median(), 5)
        self.container.add(3)
        self.container.add(4)
        self.assertEqual(self.container.get_median(), 4)

    @timeout(0.1)
    def test_02_simpleGetEvenLength(self):
        """
        Add 30, 10 -> [10, 30]
        Median of [10, 30] is 10
        Add 12, 35 -> [10, 12, 30, 35]
        Median of [10, 12, 30, 35] is 12
        Double check of median
        Add 11, 40, 100, 90 -> [10, 11, 12, 30, 35, 40, 90, 100]
        Median of [10, 11, 12, 30, 35, 40, 90, 100] is 30
        """
        self.container.add(30)
        self.container.add(10)
        self.assertEqual(self.container.get_median(), 10)
        self.container.add(12)
        self.container.add(35)
        self.assertEqual(self.container.get_median(), 12)
        self.assertEqual(self.container.get_median(), 12)
        self.container.add(11)
        self.container.add(40)
        self.container.add(100)
        self.container.add(90)
        self.assertEqual(self.container.get_median(), 30)

    @timeout(0.1)
    def test_03_simpleMixedAddAndGet(self):
        """
        Median of [] is None
        Double check of median
        Add 1 -> [1]
        Median of [1] is 1
        Add 3, 4, 2, 10, 30 -> [1, 2, 3, 4, 10, 30]
        Median of [1, 2, 3, 4, 10, 30] is 3
        Add 52, 53, 54, 55 -> [1, 2, 3, 4, 10, 30, 52, 53, 54, 55]
        Median of [1, 2, 3, 4, 10, 30, 52, 53, 54, 55] is 10
        Add 6, 7, 8, 9 -> [1, 2, 3, 4, 6, 7, 8, 9, 10, 30, 52, 53, 54, 55]
        Median of [1, 2, 3, 4, 6, 7, 8, 9, 10, 30, 52, 53, 54, 55] is 8
        Add 11 -> [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 30, 52, 53, 54, 55]
        Median of [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 30, 52, 53, 54, 55] is 9
        """
        self.assertRaises(Exception, self.container.get_median)
        self.assertRaises(Exception, self.container.get_median)
        self.container.add(1)
        self.assertEqual(self.container.get_median(), 1)
        self.container.add(3)
        self.container.add(4)
        self.container.add(2)
        self.container.add(10)
        self.container.add(30)
        self.assertEqual(self.container.get_median(), 3)
        self.container.add(52)
        self.container.add(53)
        self.container.add(54)
        self.container.add(55)
        self.assertEqual(self.container.get_median(), 10)
        self.container.add(6)
        self.container.add(7)
        self.container.add(8)
        self.container.add(9)
        self.assertEqual(self.container.get_median(), 8)
        self.container.add(11)
        self.assertEqual(self.container.get_median(), 9)

    @timeout(0.1)
    def test_04_repetitions1(self):
        """
        Add 1, 2, 3, 4, 5, 5, 5 -> [1, 2, 3, 4, 5, 5, 5]
        Median of [1, 2, 3, 4, 5, 5, 5] is 4
        Add 2 -> [1, 2, 2, 3, 4, 5, 5, 5]
        Median of [1, 2, 2, 3, 4, 5, 5, 5] is 3
        Add 3 -> [1, 2, 2, 3, 3, 4, 5, 5, 5]
        Median of [1, 2, 2, 3, 3, 4, 5, 5, 5] is 3
        Add 5, 5 -> [1, 2, 2, 3, 3, 4, 5, 5, 5, 5, 5]
        Median of [1, 2, 2, 3, 3, 4, 5, 5, 5, 5, 5] is 4
        """
        self.container.add(1)
        self.container.add(2)
        self.container.add(3)
        self.container.add(4)
        self.container.add(5)
        self.container.add(5)
        self.container.add(5)
        self.assertEqual(self.container.get_median(), 4)
        self.container.add(2)
        self.assertEqual(self.container.get_median(), 3)
        self.container.add(3)
        self.assertEqual(self.container.get_median(), 3)
        self.container.add(5)
        self.container.add(5)
        self.assertEqual(self.container.get_median(), 4)

    @timeout(0.1)
    def test_05_repetitions2(self):
        """
        Add 20 items of 42 -> [42] * 20
        Median of [42] * 20 is 42
        Add 0, 1, 2, ..., 29 -> range(30) + [42] * 20
        Median of range(30) + [42] * 20 is 24
        Add 50 items of 130 -> range(30) + [42] * 20 + [130] * 50
        Median of range(30) + [42] * 20 + [130] * 50 is 42
        Add 50 items of 170 -> range(30) + [42] * 20 + [130] * 50 + [170] * 50
        Median of range(30) + [42] * 20 + [130] * 50 + [170] * 50 is 130
        """
        for _ in range(20):
            self.container.add(42)
        self.assertEqual(self.container.get_median(), 42)
        for i in range(30):
            self.container.add(i)
        self.assertEqual(self.container.get_median(), 24)
        for _ in range(50):
            self.container.add(130)
        self.assertEqual(self.container.get_median(), 42)
        for _ in range(50):
            self.container.add(170)
        self.assertEqual(self.container.get_median(), 130)

    @timeout(0.1)
    def test_06_simpleDeletes1(self):
        """
        Add 10, 20, 30 -> [10, 20, 30]
        Delete 20 -> [10, 30]
        Median of [10, 30] is 10
        Add 5 -> [5, 10, 30]
        Median of [5, 10, 30] is 10
        Delete 30 -> [5, 10]
        Median of [5, 10] is 5
        """
        self.container.add(10)
        self.container.add(20)
        self.container.add(30)
        self.assertEqual(self.container.delete(20), True)
        self.assertEqual(self.container.get_median(), 10)
        self.container.add(5)
        self.assertEqual(self.container.get_median(), 10)
        self.assertEqual(self.container.delete(30), True)
        self.assertEqual(self.container.get_median(), 5)

    @timeout(0.1)
    def test_07_simpleDeletes2(self):
        """
        Median of [] does not exist
        Delete 5 -> []
        Median of [] is None
        Delete 5 -> []
        Add 5 -> [5]
        Median of [5] is 5
        Delete 5 -> []
        Median of [] is None
        Delete 5 -> []
        Add 5, 4, 3 -> [3, 4, 5]
        Median of [3, 4, 5] is 4
        Delete 5 -> [3, 4]
        Median of [3, 4] is 3
        Delete 5 -> [3, 4]
        Delete 3 -> [4]
        Median of [4] is 4
        """
        self.assertRaises(Exception, self.container.get_median)
        self.assertEqual(self.container.delete(5), False)
        self.assertRaises(Exception, self.container.get_median)
        self.assertEqual(self.container.delete(5), False)
        self.container.add(5)
        self.assertEqual(self.container.get_median(), 5)
        self.assertEqual(self.container.delete(5), True)
        self.assertRaises(Exception, self.container.get_median)
        self.assertEqual(self.container.delete(5), False)
        self.container.add(5)
        self.container.add(4)
        self.container.add(3)
        self.assertEqual(self.container.get_median(), 4)
        self.assertEqual(self.container.delete(5), True)
        self.assertEqual(self.container.get_median(), 3)
        self.assertEqual(self.container.delete(5), False)
        self.assertEqual(self.container.delete(3), True)
        self.assertEqual(self.container.get_median(), 4)

    @timeout(0.1)
    def test_08_repetitionsAndDeletes(self):
        """
        Add 3, 30, 30, 15 -> [3, 15, 30, 30]
        Median of [3, 15, 30, 30] is 15
        Delete 30 -> [3, 15, 30]
        Median of [3, 15, 30] is 15
        Delete 30 -> [3, 15]
        Median of [3, 15] is 3
        Add 30, 30, 30 -> [3, 15, 30, 30, 30]
        Median of [3, 15, 30, 30, 30] is 30
        Add 15 -> [3, 15, 15, 30, 30, 30]
        Median of [3, 15, 15, 30, 30, 30] is 15
        Delete 20 -> [3, 15, 15, 30, 30, 30]
        Delete 3 -> [15, 15, 30, 30, 30]
        Median of [15, 15, 30, 30, 30] is 30
        """
        self.container.add(3)
        self.container.add(30)
        self.container.add(30)
        self.container.add(15)
        self.assertEqual(self.container.get_median(), 15)
        self.assertEqual(self.container.delete(30), True)
        self.assertEqual(self.container.get_median(), 15)
        self.assertEqual(self.container.delete(30), True)
        self.assertEqual(self.container.get_median(), 3)
        self.container.add(30)
        self.container.add(30)
        self.container.add(30)
        self.assertEqual(self.container.get_median(), 30)
        self.container.add(15)
        self.assertEqual(self.container.get_median(), 15)
        self.assertEqual(self.container.delete(20), False)
        self.assertEqual(self.container.delete(3), True)
        self.assertEqual(self.container.get_median(), 30)

    @timeout(0.1)
    def test_09_mixedOperations1(self):
        """
        Add 5, 3, 5, 7, 8, 9 -> [3, 5, 5, 7, 8, 9]
        Median of [3, 5, 5, 7, 8, 9] is 5
        Delete 5, 8 -> [3, 5, 7, 9]
        Median of [3, 5, 7, 9] is 5
        Delete 5, 5 -> [3, 7, 9]
        Median of [3, 7, 9] is 7
        Add 5 -> [3, 5, 7, 9]
        Median of [3, 5, 7, 9] is 5
        Delete 5, 5, 7, 3 -> [9]
        Median of [9] is 9
        Delete 9 -> []
        Median of [] is None
        Delete 9 -> []
        Median of [] is None
        """
        self.container.add(5)
        self.container.add(3)
        self.container.add(5)
        self.container.add(7)
        self.container.add(8)
        self.container.add(9)
        self.assertEqual(self.container.get_median(), 5)
        self.assertEqual(self.container.delete(5), True)
        self.assertEqual(self.container.delete(8), True)
        self.assertEqual(self.container.get_median(), 5)
        self.assertEqual(self.container.delete(5), True)
        self.assertEqual(self.container.delete(5), False)
        self.assertEqual(self.container.get_median(), 7)
        self.container.add(5)
        self.assertEqual(self.container.get_median(), 5)
        self.assertEqual(self.container.delete(5), True)
        self.assertEqual(self.container.delete(5), False)
        self.assertEqual(self.container.delete(7), True)
        self.assertEqual(self.container.delete(3), True)
        self.assertEqual(self.container.get_median(), 9)
        self.assertEqual(self.container.delete(9), True)
        self.assertRaises(Exception, self.container.get_median)
        self.assertEqual(self.container.delete(9), False)
        self.assertRaises(Exception, self.container.get_median)

    @timeout(0.1)
    def test_10_mixedOperations2(self):
        """
        Add 0, 0, 1, 1, 2, 2, ..., 99, 99 -> 2 * range(100)
        Median of 2 * range(100) is 49
        Delete 3 items of i, median is 50 + i // 2, i in range(50)
        Container's integers are [50, 50, 51, 51, ..., 99, 99] now
        Delete range(100) -> [50, 51, ..., 99]
        Median of [50, 51, ..., 99] is 74
        """
        for i in range(100):
            self.container.add(i)
            self.container.add(i)
        self.assertEqual(self.container.get_median(), 49)
        answers = [
            50, 50, 51, 51, 52, 52, 53, 53, 54, 54, 55, 55, 56,
            56, 57, 57, 58, 58, 59, 59, 60, 60, 61, 61, 62, 62,
            63, 63, 64, 64, 65, 65, 66, 66, 67, 67, 68, 68, 69,
            69, 70, 70, 71, 71, 72, 72, 73, 73, 74, 74
        ]
        for i in range(50):
            self.assertEqual(self.container.delete(i), True)
            self.assertEqual(self.container.delete(i), True)
            self.assertEqual(self.container.delete(i), False)
            self.assertEqual(self.container.get_median(), answers[i])

        for i in range(100):
            self.assertEqual(
                self.container.delete(i),
                False if i < 50 else True
            )
        self.assertEqual(self.container.get_median(), 74)

