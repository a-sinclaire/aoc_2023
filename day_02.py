# Amelia Sinclaire 2023

from data_loader import get_data
import re


def part_one(data):
    answer = 0
    for line in data:
        game_id = int(re.findall(r'\d+', line)[0])
        subsets = re.findall(r'(?<=:).*', line)[0].split(';')
        valid_game = True
        for subset in subsets:
            color_counts = {'red': 0, 'green': 0, 'blue': 0}
            subset = subset.strip().split(',')
            for cubes in subset:
                cube = re.findall(r'\w+', cubes)
                n = int(cube[0])
                color = cube[-1]
                color_counts[color] += n
            if (color_counts['red'] > 12) or (color_counts['green'] > 13) or (color_counts['blue'] > 14):
                valid_game = False
        if valid_game:
            answer += game_id
    print(f'Part one: {answer}')
    return answer


def part_two(data):
    answer = 0
    for line in data:
        game_id = int(re.findall(r'\d+', line)[0])
        subsets = re.findall(r'(?<=:).*', line)[0].split(';')
        max_counts = {'red': 0, 'green': 0, 'blue': 0}
        for subset in subsets:
            color_counts = {'red': 0, 'green': 0, 'blue': 0}
            subset = subset.strip().split(',')
            for cubes in subset:
                cube = re.findall(r'\w+', cubes)
                n = int(cube[0])
                color = cube[-1]
                color_counts[color] += n
            colors = ['red', 'green', 'blue']
            for c in colors:
                if color_counts[c] > max_counts[c]:
                    max_counts[c] = color_counts[c]
        power = max_counts['red'] * max_counts['green'] * max_counts['blue']
        answer += power
    print(f'Part one: {answer}')
    return answer


def main():
    data, test1, test2 = get_data()
    if test1 is not None:
        print('Testing part 1...')
        assert part_one(test1) == 8
        print('Test succeeded!')
    if test2 is not None:
        print('Testing part 2...')
        assert part_two(test2) == 2286
        print('Test succeeded!')
    print('Calculating answer(s)...')
    part_one(data)
    part_two(data)


if __name__ == '__main__':
    main()
