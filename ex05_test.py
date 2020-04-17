import unittest
import numpy as np
from ex05 import FordFulkerson

class TestStringMethods(unittest.TestCase):

    def test_sample(self):
        FordFulkerson()
        self.assertTrue(1 == 1)

if __name__ == '__main__':
    unittest.main()