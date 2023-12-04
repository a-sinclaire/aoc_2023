# Amelia Sinclaire 2023

from data_loader import get_data
from tests import TestAOC
import time


def part_one(data):
    answer = 0
    return answer


def part_two(data):
    answer = 0
    return answer


def main():
    data = get_data()
    tester = TestAOC(test1_answer=-1, test2_answer=-1)
    tester.test_all()

    if data is not None:
        print('Calculating answer(s)...')
        start = time.time()
        p1 = part_one(data)
        t = time.time() - start
        print(f'Part one: {p1} in {t} seconds.')
        start = time.time()
        p2 = part_two(data)
        t = time.time() - start
        print(f'Part one: {p2} in {t} seconds.')


if __name__ == '__main__':
    main()
