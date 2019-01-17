import unittest
import numpy as np
from SwarmBots.GoalBuilding import GoalBuilding


class TestGoalBuilding(unittest.TestCase):
    """Basic test cases."""

    def setUp(self):
        self.textGrid = """
        0 0 0 0 0 0 0
        0 0 0 1 0 0 0
        0 0 1 2 1 0 0
        0 1 2 3 2 1 0
        0 0 1 2 1 0 0
        0 0 0 1 0 0 0
        0 0 0 0 0 0 0
        """
        self.resultGrid = np.array([
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 2, 1, 0, 0],
            [0, 1, 2, 3, 2, 1, 0],
            [0, 0, 1, 2, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ])

    def test_simple_grid(self):
        textGrid = self.textGrid
        resultGrid = self.resultGrid
        goalBuilding = GoalBuilding(textGrid)
        assert np.array_equal(goalBuilding.grid, resultGrid)

    def test_wrong_grid(self):
        textGrid = """
        0 0 0 0 0 0 0
        0 0 0 1 0 0 0
        0 0 1 2 1 0 0
        0 1 2 3 2 1 0
        0 0 1 2 1 0 0
        0 0 0 1 0 0 0
        0 0 0 0 0 0
        """
        self.assertRaises(ValueError, GoalBuilding, textGrid)

if __name__ == '__main__':
    unittest.main()