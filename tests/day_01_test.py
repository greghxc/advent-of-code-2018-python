import unittest
import day_01

class MyTest(unittest.TestCase):
    def test_part_one(self):
      inputs = [
        [+1, -2, +3, +1],
        [+1, +1, +1],
        [+1, +1, -2],
        [-1, -2, -3]
      ]

      expected_results = [3, 3, 0, -6]

      self.assertEqual([day_01.part_one(i) for i in inputs], expected_results)

    def test_part_two(self):
      inputs = [
                [+1, -2, +3, +1],
                [+1, -1],
                [+3, +3, +4, -2, -4],
                [-6, +3, +8, +5, -6],
                [+7, +7, -2, -7, -4]
      ]

      expected_results = [2, 0, 10, 5, 14]

      self.assertEqual([day_01.part_two(i) for i in inputs], expected_results)