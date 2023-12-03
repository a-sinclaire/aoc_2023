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
    data, test1, test2 = get_data()
    test1_answer = -1
    test2_answer = -1
    tester = TestAOC(part_one, part_two, test1, test1_answer, test2, test2_answer)
    tester.test_part_one()
    tester.test_part_two()

    if data is not None:
        print('Calculating answer(s)...')
        print(f'Part one: {part_one(data)}')
        print(f'Part two: {part_two(data)}')


if __name__ == '__main__':
    main()
