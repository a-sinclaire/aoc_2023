# Amelia Sinclaire 2023

from data_loader import get_data
from tests import TestAOC


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
        print(f'Part one: {part_one(data)}')
        print(f'Part two: {part_two(data)}')


if __name__ == '__main__':
    main()
