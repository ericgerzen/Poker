import random
import time

cards = {'2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'Tc', 'Jc', 'Qc', 'Kc', 'Ac',
         '2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', 'Td', 'Jd', 'Qd', 'Kd', 'Ad',
         '2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', 'Th', 'Jh', 'Qh', 'Kh', 'Ah',
         '2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 'Ts', 'Js', 'Qs', 'Ks', 'As'}

hand_0 = random.choice(list(cards))
cards.remove(hand_0)
hand_1 = random.choice(list(cards))
cards.remove(hand_1)
hand_2 = random.choice(list(cards))
cards.remove(hand_2)
hand_3 = random.choice(list(cards))
cards.remove(hand_3)

print(f'Your hand is: {hand_0}, {hand_1}')

flop_0 = random.choice(list(cards))
cards.remove(flop_0)
flop_1 = random.choice(list(cards))
cards.remove(flop_1)
flop_2 = random.choice(list(cards))
cards.remove(flop_2)
turn = random.choice(list(cards))
cards.remove(turn)
river = random.choice(list(cards))
cards.remove(river)

print('The flop shows: ', flop_0, flop_1, flop_2)
time.sleep(2)
print('The turn shows: ', flop_0, flop_1, flop_2, turn)
time.sleep(2)
print('The river shows: ', flop_0, flop_1, flop_2, turn, river)
time.sleep(2)

print('Your hand is: ', hand_0, hand_1)
time.sleep(2)
print('You are up against: ', hand_2, hand_3)







