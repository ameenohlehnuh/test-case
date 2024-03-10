from coe_number.number_utils import is_prime_list
import unittest

class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
        

    def test_give_0_2_3_is_prime(self):
        none_prime_list = [0, 2, 3]
        is_not_prime = is_prime_list(none_prime_list)
        self.assertFalse(is_not_prime)
        

    def test_give_2_5_7_11_is_prime(self):
        prime_list = [2,5,7,11]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
        

    def test_give_5_10_15_20_is_prime(self):
        none_prime_list = [5,10,15,20]
        is_not_prime = is_prime_list(none_prime_list)
        self.assertFalse(is_not_prime)
        

    def test_give_13_17_19_is_prime(self):
        prime_list = [13,17,19]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)