# Amelia Sinclaire 2023

import unittest


class TestAOC(unittest.TestCase):
    def __init__(self, part_one, part_two, test1=None, test1_answer=-1, test2=None, test2_answer=-1):
        super().__init__()
        self.partOne = part_one
        self.test1data = test1
        self.test1answer = test1_answer

        self.partTwo = part_two
        self.test2data = test2
        self.test2answer = test2_answer

    def test_part_one(self):
        print(f'Testing part one...')
        if self.test1data is None:
            print(f'No test data found for part one')
            return
        self.assertEquals(self.partOne(self.test1data), self.test1answer)
        print('Test one passed!')

    def test_part_two(self):
        print(f'Testing part two...')
        if self.test2data is None:
            print(f'No test data found for part two')
            return
        self.assertEquals(self.partTwo(self.test2data), self.test2answer)
        print('Test two passed!')
