# Amelia Sinclaire 2023

import unittest
import __main__
from data_loader import get_test_data


class TestAOC(unittest.TestCase):
    def __init__(self, test1_answer=-1, test2_answer=-1):
        super().__init__()
        self.partOne = __main__.part_one
        self.partTwo = __main__.part_two

        self.test1data, self.test2data = get_test_data()

        self.test1answer = test1_answer
        self.test2answer = test2_answer

    def test_part_one(self):
        print(f'Testing part one...')
        if self.test1data is None:
            print(f'No test data found for part one')
            return False
        self.assertEquals(self.partOne(self.test1data), self.test1answer)
        print('Test one passed!')
        return True

    def test_part_two(self):
        print(f'Testing part two...')
        if self.test2data is None:
            print(f'No test data found for part two')
            return False
        self.assertEquals(self.partTwo(self.test2data), self.test2answer)
        print('Test two passed!')
        return True

    def test_all(self):
        self.test_part_one()
        self.test_part_two()
        print('---')
