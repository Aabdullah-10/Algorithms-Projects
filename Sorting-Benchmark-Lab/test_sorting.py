import unittest
from sorting_benchmark import algorithms


class TestSorting(unittest.TestCase):

    def test_sorting_algorithms(self):
        cases = [
            [],
            [5],
            [4, 2, 4, 1],
            [1, 2, 3, 4],
            [4, 3, 2, 1],
            [-5, 3, -1, 0]
        ]

        for algorithm in algorithms.values():
            for data in cases:
                self.assertEqual(algorithm(data), sorted(data))


if __name__ == "__main__":
    unittest.main()
