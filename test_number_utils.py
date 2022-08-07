from coe_number.number_utils import is_prime_list

import unittest

class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_is_prime(self):
        prime_list = [1, 2, 3]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    def test_give_5_7_11_is_prime(self):
        prime_list = [5, 7, 11]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    def test_give_23_19_17_is_prime(self):
        prime_list = [23, 19, 17]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    def test_give_41_43_71_is_prime(self):
        prime_list = [41, 43, 71]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    def test_give_23_37_73_is_prime(self):
        prime_list = [23, 37, 73]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
    def test_give_97_67_41_is_prime(self):
        prime_list = [97, 67, 41]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)
 