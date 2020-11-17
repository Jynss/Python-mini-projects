import unittest

from primeception import *


class MyTestCase(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(is_prime(-100))
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertFalse(is_prime(6))
        self.assertTrue(is_prime(7))
        self.assertFalse(is_prime(8))
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(12))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(89))
        self.assertFalse(is_prime(90))

    def test_is_prime_ception(self):
        self.assertFalse(is_prime_ception([]))
        self.assertFalse(is_prime_ception([2]))
        self.assertFalse(is_prime_ception([4]))
        self.assertFalse(is_prime_ception([4, 4]))
        self.assertFalse(is_prime_ception([4, 6]))
        self.assertFalse(is_prime_ception([2, 4]))
        self.assertFalse(is_prime_ception([4, 2]))
        self.assertTrue(is_prime_ception([2, 2]))
        self.assertTrue(is_prime_ception([2, 3]))
        self.assertTrue(is_prime_ception([3, 2]))
        self.assertTrue(is_prime_ception([3, 3]))
        self.assertTrue(is_prime_ception([2, 3, 5]))
        self.assertTrue(is_prime_ception([7, 7, 7]))
        self.assertTrue(is_prime_ception([7, 7, 1]))
        self.assertFalse(is_prime_ception([1, 7, 1]))
        self.assertFalse(is_prime_ception([2, 4, 6]))
        self.assertFalse(is_prime_ception([2, 4, 6, 8]))
        self.assertTrue(is_prime_ception([2, 3, 4, 5]))
        self.assertFalse(is_prime_ception(list(range(11))))
        self.assertTrue(is_prime_ception(list(range(12))))


if __name__ == '__main__':
    unittest.main()
