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


def adjacent_symbols(number, last_line, current_line, next_line):
    number_start = number.start()
    number_end = number.end()-1

    # find location of symbols that are not numbers or periods in lines
    last_symbols = list(re.finditer(r'[^\d.\s]', last_line)) if last_line is not None else []
    current_symbols = list(re.finditer(r'[^\d.\s]', current_line))
    next_symbols = list(re.finditer(r'[^\d.\s]', next_line)) if next_line is not None else []
    symbols = []
    for symbol in (last_symbols + current_symbols + next_symbols):
        symbol_location = symbol.start()
        if (symbol_location - 1 <= number_start <= symbol_location + 1) or (symbol_location - 1 <= number_end <= symbol_location + 1):
            symbols.append(symbol.group())
    return symbols


def part_one(data):
    answer = 0
    for idx, current_line in enumerate(data):
        last_line = data[idx - 1] if idx > 0 else None
        next_line = data[idx + 1] if idx < len(data) - 1 else None
        # find location of numbers in this line
        numbers = list(re.finditer(r'\d+', current_line))
        for num in numbers:
            symbols = adjacent_symbols(num, last_line, current_line, next_line)
            if len(symbols) > 0:
                answer += int(num.group())
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
    data = get_data()
    tester = TestAOC(test1_answer=4361, test2_answer=467835)
    tester.test_all()

    if data is not None:
        print('Calculating answer(s)...')
        print(f'Part one: {part_one(data)}')
        print(f'Part two: {part_two(data)}')


if __name__ == '__main__':
    main()
