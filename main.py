import sys
import time

from random import randint
from spot import Spot

size = 10
holes = 3
monsters = 2

world = [[Spot() for i in range(size)] for i in range(size)]

def print_gold():
    c = randint(0, size - 1)
    r = randint(0, size - 1)
    spot = world[c][r]
    spot.contains = Spot.GOLD
    world[c][r] = spot

def print_point(type):
    if type is Spot.HOLE:
        items = 3
    elif type is Spot.MONSTER:
        items = 2

    for _ in range(items):
        c = randint(0, size - 1)
        r = randint(0, size - 1)
        spot = world[c][r]
        spot.contains = type
        world[c][r] = spot

        if c < size - 1:
            world[c + 1][r].set_clue(type)
        if c > 0:
            world[c - 1][r].set_clue(type)

        if r < size - 1:
            world[c][r + 1].set_clue(type)
        if r > 0:
            world[c][r - 1].set_clue(type)


print_point(Spot.HOLE)
print_point(Spot.MONSTER)
print_gold()


'''
for i in range(10):
    sys.stdout.flush()
    for r in world:
        for s in r:
            sys.stdout.write(str(s))
        sys.stdout.write('\n')    
    time.sleep(0.5)
'''
