import unittest
from main import is_prime_v4 as is_prime


class PrimeTest(unittest.TestCase):

    #素数
    def test_prime_ok(self):
        for i in [2, 3, 5, 7, 11, 13, 17, 19]:
            self.assertTrue(is_prime(i))
    #素数以外
    def test_is_prime_no(self):
        for i in [1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]:
            self.assertFalse(is_prime(i))
    #負数
    def test_is_prime_negative(self):
        self.assertFalse(is_prime(-1))

    #数字以外
    def test_is_prime_raise_typeerror(self):
        with self.assertRaises(TypeError):
            is_prime('string')


if __name__ == '__main__':
    unittest.main()
