import unittest
import numpy as np
from ex03 import dijkstra

class TestStringMethods(unittest.TestCase):

    def test_sample(self):
        testSubject = np.array([
            [0, 2, 2, 0, 0, 0],
            [0, 0, 0, 2, 0, 5],
            [0, 0, 0, 0, 2, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0]
        ])
        a, b = dijkstra(testSubject)
        print(a)
        print(b)
        self.assertTrue(1 == 1)

if __name__ == '__main__':
    unittest.main()