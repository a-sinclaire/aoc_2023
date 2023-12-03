# Amelia Sinclaire 2023

from data_loader import get_data
from tests import TestAOC
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
    test1_answer = 4361
    test2_answer = 467835
    tester = TestAOC(part_one, part_two, test1, test1_answer, test2, test2_answer)
    tester.test_part_one()
    tester.test_part_two()

    if data is not None:
        print('Calculating answer(s)...')
        print(f'Part one: {part_one(data)}')
        print(f'Part two: {part_two(data)}')


if __name__ == '__main__':
    main()
