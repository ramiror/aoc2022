pos=[(0,0)] * 10

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
        pos[0] = tuple(np.add(pos[0], delta[direction]))
        for knot in range(1,len(pos)):
            pos[knot] = update_tail(pos[knot-1], pos[knot])
        trail.add(pos[len(pos)-1])
print(len(trail))
