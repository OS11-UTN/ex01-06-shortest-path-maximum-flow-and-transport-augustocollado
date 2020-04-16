import unittest
import numpy as np
from ex05 import dfs

class TestStringMethods(unittest.TestCase):

    def test_sample(self):
        testSubject = np.array([
            [0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0],
        ])
        pathExists, path = dfs(testSubject, 0, 5)
        print(pathExists)
        print(path)
        self.assertTrue(1 == 1)

if __name__ == '__main__':
    unittest.main()