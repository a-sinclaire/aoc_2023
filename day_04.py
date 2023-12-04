# Amelia Sinclaire 2023

from data_loader import get_data
from tests import TestAOC
import time


def part_one(data):
    answer = 0
    for card in data:
        card_points = 0
        card_data = card.split(':')[1].split('|')
        winning_numbers = card_data[0].split()
        my_numbers = card_data[1].split()
        for my_number in my_numbers:
            if my_number in winning_numbers:
                card_points = 1 if card_points == 0 else card_points*2
        answer += card_points
    return answer


def part_two(data):
    all_cards = []
    for card in data:
        card_data = card.split(':')
        card_id = int(card_data[0].split()[1])
        all_cards.append(card_id)
        winning_numbers = card_data[1].split('|')[0].split()
        my_numbers = card_data[1].split('|')[1].split()
        matching_nums = 0
        for my_number in my_numbers:
            if my_number in winning_numbers:
                matching_nums += 1
        cards_to_add = []
        for m in range(matching_nums):
            copy_to_win = card_id+1+m
            if copy_to_win <= len(data):
                # add one for every instance of this card in all_cards
                cards_to_add.extend([copy_to_win]*all_cards.count(card_id))
        all_cards.extend(cards_to_add)
    return len(all_cards)


def main():
    data = get_data()
    tester = TestAOC(test1_answer=13, test2_answer=30)
    tester.test_all()

    if data is not None:
        print('Calculating answer(s)...')
        start = time.time()
        p1 = part_one(data)
        t = time.time() - start
        print(f'Part one: {p1} in {t} seconds.')
        start = time.time()
        p2 = part_two(data)
        t = time.time() - start
        print(f'Part one: {p2} in {t} seconds.')


if __name__ == '__main__':
    main()
