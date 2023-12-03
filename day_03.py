# Amelia Sinclaire 2023

from data_loader import get_data
import re


def adjacent_numbers(symbol, last_line, current_line, next_line):
    symbol_location = symbol.start()
    last_numbers = list(re.finditer(r'\d+', last_line))
    current_numbers = list(re.finditer(r'\d+', current_line))
    next_numbers = list(re.finditer(r'\d+', next_line))
    numbers = []
    for number in (last_numbers + current_numbers + next_numbers):
        start, end = number.span()
        end -= 1
        if (symbol_location-1 <= start <= symbol_location+1) or (symbol_location-1 <= end <= symbol_location+1):
            numbers.append(number.group())
    return numbers


def part_one(data):
    answer = 0
    for idx, current_line in enumerate(data):
        last_line = data[idx-1] if idx > 0 else None
        next_line = data[idx+1] if idx < len(data)-1 else None
        # find location of symbols that are not numbers or periods
        symbols = list(re.finditer(r'[^\d.\s]', current_line))
        for symbol in symbols:
            nums = adjacent_numbers(symbol, last_line, current_line, next_line)
            for n in nums:
                answer += int(n)
    return answer


def part_two(data):
    answer = 0
    for idx, current_line in enumerate(data):
        last_line = data[idx - 1] if idx > 0 else None
        next_line = data[idx + 1] if idx < len(data) - 1 else None
        # find location of all * symbols
        symbols = list(re.finditer(r'[*]', current_line))
        for symbol in symbols:
            nums = adjacent_numbers(symbol, last_line, current_line, next_line)
            if len(nums) == 2:
                answer += int(nums[0]) * int(nums[1])
    return answer


def main():
    data, test1, test2 = get_data()
    if test1 is not None:
        print('Testing part 1...')
        test_1_expected = 4361
        test_1_actual = part_one(test1)
        if test_1_actual != test_1_expected:
            raise Exception(f'Assertion Failed: Expected {test_1_expected} but got {test_1_actual}.')
        print('Test 1 succeeded!')
    if test2 is not None:
        print('Testing part 2...')
        test_2_expected = 467835
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
