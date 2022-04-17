import mock
import unittest
from solution import Solution


class SolutionCase(unittest.TestCase):

    def test_twoSum(self):
        solution = Solution()
        nums = [2, 7, 11, 15]
        target = 9

        expected_output = [0, 1]
        self.assertEqual(solution.twoSum(nums, target), expected_output)

        nums = [3, 2, 4]
        target = 6

        expected_output = [1, 2]
        self.assertEqual(solution.twoSum(nums, target), expected_output)


def main():
    """docstring for main"""
    unittest.main()


if __name__ == '__main__':
    main()
