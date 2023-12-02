# Amelia Sinclaire 2023

from data_loader import get_data


def part_one(data):
    answer = 0
    print(f'Part one: {answer}')
    return answer


def part_two(data):
    answer = 0
    print(f'Part two: {answer}')
    return answer


def main():
    data, test1, test2 = get_data()
    if test1 is not None:
        print('Testing part 1...')
        assert part_one(test1) == 8
        print('Test succeeded!')
    if test2 is not None:
        print('Testing part 2...')
        assert part_two(test2) == 0
        print('Test succeeded!')
    print('Calculating answer(s)...')
    part_one(data)
    part_two(data)


if __name__ == '__main__':
    main()
