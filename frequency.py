import random
from collections import Counter

cards = ['2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'Tc', 'Jc', 'Qc', 'Kc', 'Ac',
         '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', 'Td', 'Jd', 'Qd', 'Kd', 'Ad',
         '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', 'Th', 'Jh', 'Qh', 'Kh', 'Ah',
         '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 'Ts', 'Js', 'Qs', 'Ks', 'As']


straights = ['A2345', '23456', '34567', '45678', '56789', '6789T', '789TJ', '89TJQ', '9TJQK', 'TJQKA']

chosen_cards = []

for i in range(7):
    card = random.choice(cards)
    chosen_cards.append(card)
    cards.remove(card)

results = {
    'highcard': 0,
    'pair': 0,
    'twopair': 0,
    'toak': 0,
    'straight': 0,
    'flush': 0,
    'fullhouse': 0,
    'quads': 0,
    'straightflush': 0,
    'royalflush': 0
}

def hand_checker(hand):

    highcard = False
    pair = False
    pair_count = 0
    twopair = False
    twopair_count = 0
    toak = False
    toak_count = 0
    straight = False
    flush = False
    fullhouse = False
    quads = False
    straightflush = False
    royalflush = False

    ranks = [c[0] for c in hand]
    suits = [c[1] for c in hand]
    count_suits = Counter(suits)
    count_ranks = Counter(ranks)

    for suit, count in count_suits.items():
        if count >= 5:
            flush = True

    rank_order = '23456789TJQKA'
    ace_low_order = 'A23456789TJQK'
    unique_ranks = sorted(set(ranks), key=lambda x: rank_order.index(x))
    rank_string = ''.join(unique_ranks)
    if 'A' in unique_ranks:
        unique_ranks_ace_low = sorted(set(ranks), key=lambda x: ace_low_order.index(x))
        rank_string_ace_low = ''.join(unique_ranks_ace_low)
    else:
        rank_string_ace_low = None

    found_straight = False
    for s in straights:
        if s in rank_string or (rank_string_ace_low and s in rank_string_ace_low):
            found_straight = True
            break
    straight = found_straight

    rank_order = '23456789TJQKA'
    ace_low_order = 'A23456789TJQK'

    for suit, count in count_suits.items():
        if count >= 5:
            suited_ranks = [r for r, s in zip(ranks, suits) if s == suit]
            unique_suited_ranks = sorted(set(suited_ranks), key=lambda x: rank_order.index(x))
            suited_rank_str = ''.join(unique_suited_ranks)
            if 'A' in unique_suited_ranks:
                suited_rank_str_ace_low = ''.join(sorted(set(suited_ranks), key=lambda x: ace_low_order.index(x)))
            else:
                suited_rank_str_ace_low = None
            for s in straights:
                if s in suited_rank_str or (suited_rank_str_ace_low and s in suited_rank_str_ace_low):
                    straightflush = True
                    if s == 'TJQKA':
                        royalflush = True
                    break

    for rank, count in count_ranks.items():
        if count == 2 and not flush and not straight:
            pair_count += 1
            pair = True
        if count == 3 and not flush and not straight:
            toak_count += 1
            toak = True

    if 3 in count_ranks.values() and 2 in count_ranks.values():
        fullhouse = True
        toak_count = 0
        toak = False
        pair_count = 0
        pair = False

    if 4 in count_ranks.values():
        quads = True
        toak_count = 0
        toak = False
        pair_count = 0
        pair = False

    if pair_count == 2 and not quads and not flush and not straight:
        twopair_count += 1
        twopair = True
        pair_count = 0
        pair = False

    if royalflush:
        return 'royalflush'
    elif straightflush:
        return 'straightflush'
    elif quads:
        return 'quads'
    elif fullhouse:
        return 'fullhouse'
    elif flush:
        return 'flush'
    elif straight:
        return 'straight'
    elif toak:
        return 'toak'
    elif twopair:
        return 'twopair'
    elif pair:
        return 'pair'
    else:
        return 'highcard'

n = 100000
for _ in range(n):
    deck = cards.copy()
    hand = []
    for i in range(7):
        card = random.choice(deck)
        hand.append(card)
        deck.remove(card)
    hand_type = hand_checker(hand)
    results[hand_type] += 1

print(results)
