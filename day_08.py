# Amelia Sinclaire 2023
import itertools
from math import lcm

from data_loader import get_data
from tests import TestAOC
from timing import time_it_decorator
time_it_decorator.enabled = True


@time_it_decorator
def part_one(data):
    instructions = data[0].strip()
    maps = data[2:]
    map_dict = {}
    for m in maps:
        start, end = m.split('=')
        left, right = end.replace('(', '').replace(')', '').split(',')
        map_dict[start.strip()] = (left.strip(), right.strip())

    m = 'AAA'
    count = 0
    for instruction in itertools.cycle(instructions):
        # if count > 5_000 and count % 5_000 == 0:
        #     print(count)
        if m == 'ZZZ':
            break
        count += 1
        if instruction == 'L':
            m = map_dict[m][0]
            continue
        m = map_dict[m][1]
    return count


@time_it_decorator
def part_two(data):
    instructions = data[0].strip()
    maps = data[2:]
    map_dict = {}
    for m in maps:
        start, end = m.split('=')
        left, right = end.replace('(', '').replace(')', '').split(',')
        map_dict[start.strip()] = (left.strip(), right.strip())

    all_paths = []
    for k in map_dict.keys():
        if k[2] == 'A':
            all_paths.append([k])
    done_paths = []

    for instruction in itertools.cycle(instructions):
        for p in all_paths:
            if p[-1][2] == 'Z':
                done_paths.append(p)
                all_paths.remove(p)
        if len(all_paths) == 0:
            break

        new_paths = []
        for p in all_paths:
            m = p[-1]
            if instruction == 'L':
                left = map_dict[m][0]
                p.append(left)
                new_paths.append(p)
                continue
            right = map_dict[m][1]
            p.append(right)
            new_paths.append(p)
        all_paths = new_paths

    steps_to_z = ([len(x)-1 for x in done_paths])
    return lcm(*steps_to_z)


def main():
    data = get_data()
    tester = TestAOC(test1_answer=6, test2_answer=6)
    tester.test_all()

    if data is not None:
        print('Calculating answer(s)...')
        print(f'Part one: {part_one(data)}')
        print(f'Part two: {part_two(data)}')


if __name__ == '__main__':
    main()
