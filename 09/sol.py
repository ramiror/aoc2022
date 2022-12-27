tpos=(0,0)
hpos=(0,0)

delta = {
        'U': (-1, 0),
        'D': ( 1, 0),
        'R': ( 0, 1),
        'L': ( 0,-1)
        }

import numpy as np

def update_tail(hpos, tpos):
    movement = (0,0)
    tension = tuple(np.subtract(hpos, tpos))
    if abs(tension[0]) > 1 or abs(tension[1]) > 1:
        movement = np.sign(tension)
    tpos = tuple(np.add(tpos, movement))
    return tpos

import sys
trail=set()
for line in sys.stdin.readlines():
    direction, amount = line.split()
    #print(direction, amount)
    for step in range(int(amount)):
        hpos = tuple(np.add(hpos, delta[direction]))
        tpos = update_tail(hpos, tpos)
        trail.add(tpos)
print(len(trail))


