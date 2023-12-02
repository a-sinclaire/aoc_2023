# Amelia Sinclaire 2023

import re
from data_loader import get_data
data = get_data()


def part_one():
    total = 0
    for line in data:
        numbers = re.findall(r'[0-9]', line)
        total += int(numbers[0] + numbers[-1])
    print(total)


def part_two():
    total = 0
    idx_to_int_forward = [None, 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    idx_to_int_bakward = [None, 'eno', 'owt', 'eerht', 'ruof', 'evif', 'xis', 'neves', 'thgie', 'enin']
    for line in data:
        first_numbr = re.search(r'one|two|three|four|five|six|seven|eight|nine|[0-9]', line).group()
        last_number = re.search(r'eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|[0-9]', line[::-1]).group()
        if len(first_numbr) > 1:
            first_numbr = str(idx_to_int_forward.index(first_numbr))
        if len(last_number) > 1:
            last_number = str(idx_to_int_bakward.index(last_number))
        total += int(first_numbr + last_number)
    print(total)


if __name__ == '__main__':
    part_one()
    part_two()
