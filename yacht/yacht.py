YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    dice = sorted(dice, key=dice.count, reverse=True)
    return {
        0: 50 if len(set(dice)) == 1 else 0,
        1: dice.count(1),
        2: dice.count(2)*2,
        3: dice.count(3)*3,
        4: dice.count(4)*4,
        5: dice.count(5)*5,
        6: dice.count(6)*6,
        7: sum(dice) if len(set(dice)) == 2 and dice.count(dice[0]) == 3 else 0,
        8: dice[0]*4 if len(set(dice)) <= 2 and dice.count(dice[0]) >= 4 else 0,
        9: 30 if len(set(dice)) == 5 and 6 not in dice else 0,
        10: 30 if len(set(dice)) == 5 and 1 not in dice else 0,
        11: sum(dice)
    }[category]