# Amelia Sinclaire 2023

from data_loader import get_data


def part_one(data):
    answer = 0
    return answer


def part_two(data):
    answer = 0
    return answer


def main():
    data, test1, test2 = get_data()
    if test1 is not None:
        print('Testing part 1...')
        test_1_expected = -1
        test_1_actual = part_one(test1)
        if test_1_actual != test_1_expected:
            raise Exception(f'Assertion Failed: Expected {test_1_expected} but got {test_1_actual}.')
        print('Test 1 succeeded!')
    if test2 is not None:
        print('Testing part 2...')
        test_2_expected = -1
        test_2_actual = part_two(test1)
        if test_2_actual != test_2_expected:
            raise Exception(f'Assertion Failed: Expected {test_2_expected} but got {test_2_actual}.')
        print('Test 2 succeeded!')
    if data is not None:
        print('Calculating answer(s)...')
        print(f'Part one: {part_one(data)}')
        print(f'Part two: {part_two(data)}')


if __name__ == '__main__':
    main()
