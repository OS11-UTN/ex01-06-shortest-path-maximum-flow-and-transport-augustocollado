import unittest
import numpy as np
from basic_utils import nn2na

class TestStringMethods(unittest.TestCase):

    def test_sample(self):
        testSubject = np.array([[0, 1, 1],[0, 0, 0],[0, 0, 0]])
        result = nn2na(testSubject)
        expected = [[1, 1], [-1, 0], [0, -1]]
        self.assertTrue((result == expected).all())

if __name__ == '__main__':
    unittest.main()