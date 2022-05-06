import random

# Returns a list of rolled die and their sum.
def ndicen(count,sides) :
    dice = []
    for die in range(count) :
        pips = random.randint(1, sides)
        dice.append(pips)
    return(dice, sum(dice))