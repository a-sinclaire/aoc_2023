# Amelia Sinclaire 2023
import itertools
from collections import Counter
from enum import Enum
import re

from data_loader import get_data
from tests import TestAOC
from timing import time_it_decorator
time_it_decorator.enabled = True

HandType = Enum('HandType',
                ['HighCard', 'OnePair', 'TwoPair', 'ThreeOfAKind', 'FullHouse', 'FourOfAKind', 'FiveOfAKind'])
AllCards = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
AllCards2 = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']


def upgrade_hand(hand):
    card_counts = Counter(hand)
    if card_counts.get('J', 0) == 0:
        return hand
    num_j = card_counts.get('J')
    permutations = list(itertools.combinations_with_replacement([c for c in AllCards if c != 'J'], r=num_j))
    js = list(re.finditer(r'J', hand))
    best_hand = None
    for p in permutations:
        new_hand = [c for c in hand]
        for idx, j in enumerate(js):
            new_hand[int(j.start())] = p[idx]
        if best_hand is None:
            best_hand = new_hand
            continue
        if score_hand_type(get_hand_type(new_hand)) > score_hand_type(get_hand_type(best_hand)):
            best_hand = new_hand
    return ''.join(best_hand)


def get_hand_type(hand):
    card_counts = Counter(hand)
    match_counts = sorted(list(card_counts.values()), reverse=True)
    match len(match_counts):
        case 1: return HandType.FiveOfAKind
        case 2:  # 4 kind or full house
            for n in match_counts:
                if n == 4:
                    return HandType.FourOfAKind
            return HandType.FullHouse
        case 3:  # 3 kind or 2 pair
            for n in match_counts:
                if n == 3:
                    return HandType.ThreeOfAKind
            return HandType.TwoPair
        case 4: return HandType.OnePair
        case 5: return HandType.HighCard
        case default: raise Exception('INVALID HAND -- CANNOT DETERMINE TYPE')


def score_hand_type(hand):
    return get_hand_type(hand).value


def score_cards(hand, is_part_one=True):
    my_sum = 0
    for idx, card in enumerate(hand):
        if is_part_one:
            card_value = AllCards.index(card) + 1
        else:
            card_value = AllCards2.index(card) + 1
        my_sum += card_value * (15 ** (5 - idx))
    return my_sum


@time_it_decorator
def part_one(data):
    hands = [(y[0], y[1]) for y in [x.split() for x in data]]
    rank = sorted(hands, key=lambda h: (score_hand_type(h[0]), score_cards(h[0])))
    return sum([int(h[1])*(i+1) for i, h in enumerate(rank)])


@time_it_decorator
def part_two(data):
    hands = [(y[0], y[1]) for y in [x.split() for x in data]]
    rank = sorted(hands, key=lambda h: (score_hand_type(upgrade_hand(h[0])), score_cards(h[0], is_part_one=False)))
    return sum([int(h[1]) * (i + 1) for i, h in enumerate(rank)])


def main():
    data = get_data()
    tester = TestAOC(test1_answer=6440, test2_answer=5905)
    tester.test_all()

    if data is not None:
        print('Calculating answer(s)...')
        print(f'Part one: {part_one(data)}')
        print(f'Part two: {part_two(data)}')


if __name__ == '__main__':
    main()
