import random
import time
from collections import Counter

cards = ['2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'Tc', 'Jc', 'Qc', 'Kc', 'Ac',
         '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', 'Td', 'Jd', 'Qd', 'Kd', 'Ad',
         '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', 'Th', 'Jh', 'Qh', 'Kh', 'Ah',
         '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 'Ts', 'Js', 'Qs', 'Ks', 'As']

straights = {'A2345': 1,
             '23456': 2,
             '34567': 3,
             '45678': 4,
             '56789': 5,
             '6789T': 6,
             '789TJ': 7,
             '89TJQ': 8,
             '9TJQK': 9,
             'TJQKA': 10}

players = int(input('How many players are you up against? '))

print('Okay')
time.sleep(2)

print('Type your hand in the the format Ns, where N represents the value of your card, '
      'and s represents its suit. Do it twice.')

time.sleep(5)

while True:
    card_1 = input('Type your first card ')

    if card_1 not in cards:
        print('This card is invalid. Remember to use the format Ns. Example: As')

    else:
        break
cards.remove(card_1)

while True:
    card_2 = input('Type your second card ')

    if card_2 not in cards:
        print('This card is invalid. Remember to use the format Ns. Example: As')

    else:
        break
cards.remove(card_2)

while True:
    flop_1 = input('Type the first flop card ')

    if flop_1 not in cards:
        print('This card is invalid. Remember to use the format Ns. Example: As')

    else:
        break
cards.remove(flop_1)

while True:
    flop_2 = input('Type the second flop card ')

    if flop_2 not in cards:
        print('This card is invalid. Remember to use the format Ns. Example: As')

    else:
        break
cards.remove(flop_2)

while True:
    flop_3 = input('Type the third flop card ')

    if flop_3 not in cards:
        print('This card is invalid. Remember to use the format Ns. Example: As')

    else:
        break
cards.remove(flop_3)

while True:
    turn = input('Type the turn card ')

    if turn not in cards:
        print('This card is invalid. Remember to use the format Ns. Example: As')

    else:
        break
cards.remove(turn)

while True:
    river = input('Type the river card ')

    if river not in cards:
        print('This card is invalid. Remember to use the format Ns. Example: As')

    else:
        break
cards.remove(river)

available_cards = [card_1, card_2, flop_1, flop_2, flop_3, turn, river]

hands = {'highcard': 1,
         'pair': 2,
         'twopair': 3,
         'set': 4,
         'straight': 5,
         'flush': 6,
         'fullhouse': 7,
         'quads': 8,
         'straightflush': 9}

def hand_checker(hand):
    ranks = [c[0] for c in hand]
    suits = [c[1] for c in hand]
    count_suits = Counter(suits)
    for suit in count_suits:
        if suit.value >= 5:
            print('There is a flush with ', suit)
            break
    count_ranks = Counter(ranks)
    for rank in count_ranks:
        if rank.value == 2:
            print('There is a pair with ', rank)
        elif rank.value == 3:
            print('There is a set with ', rank)
        elif rank.value == 4:
            print('There is quads with ', rank)

print(hand_checker(available_cards))




