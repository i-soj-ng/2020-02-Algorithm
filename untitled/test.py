import random

for dice1 in range(1, 7):
    for dice2 in range(1, 7):

        if dice1 + dice2 == 6:
            print(dice1, dice2)

#중복되는 경우 없애기기