# Amelia Sinclaire 2023

from data_loader import get_data
from tests import TestAOC
from timing import time_it_decorator


def distance(hold_time, race_time):
    return hold_time*(race_time-hold_time)


@time_it_decorator
def part_one(data):
    answer = 1
    race_times = [int(x) for x in data[0].split(':')[1].strip().split()]
    records = [int(x) for x in data[1].split(':')[1].strip().split()]
    races = zip(race_times, records)
    for idx, race in enumerate(races):
        race_time, record = race
        winning_hold_times = [x for x in range(race_time) if distance(x, race_time) > record]
        answer *= len(winning_hold_times)
    return answer


@time_it_decorator
def part_two(data):
    race_time = int(data[0].split(':')[1].replace(' ', ''))
    record = int(data[1].split(':')[1].replace(' ', ''))
    winning_hold_times = [x for x in range(race_time) if distance(x, race_time) > record]
    answer = len(winning_hold_times)
    return answer


def main():
    data = get_data()
    time_it_decorator.enabled = True
    tester = TestAOC(test1_answer=288, test2_answer=71503)
    tester.test_all()

    if data is not None:
        print('Calculating answer(s)...')
        print(f'Part one: {part_one(data)}')
        print(f'Part two: {part_two(data)}')


if __name__ == '__main__':
    main()
