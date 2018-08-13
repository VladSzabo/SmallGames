from pygame import *
from random import *
from json import *

"""
    s -> shapes
    s = [
        shape,
        shape, ...
    ] where
        shape = [rotation1 (, rotation2, ...)]
        rotation<i> = [[1's and 0's], [1's and 0's], ...]
        
    g = game screen
    m = map (20x10)
    
    c = current shape
    r = current rotation
    
    x, y = x and y pos of the top left corner of the shape
    
    For now, we separate variables for clarity but we keep short names to check if it fits
"""

s = [[[i+[0]*20 for i in r]+[[0]*20]*20 for r in s] for s in loads(open("s").read())]
m = [[randint(0, 0) for _ in range(10)] for _ in range(99)]
m[randint(0, 19)] = [1]*10
m[randint(0, 19)] = [1]*10
g = display.set_mode((200, 400))
c, r = s[2], 0
x, y, u = 3, 0, KEYUP

print({0: 1 for a in range(3)}.get(0))

while True:
    # handle movement and rotation
    x, r = [[{1: (x+1, r), 2: (x-1, r), 0: (x, r+1)}.get(e.key-274) for e in event.get() if e.type == u]+[(x, r)]][0][0]

    # draw map
    [[draw.rect(g, [0, 255][m[i][j]], (j*20, i*20, 20, 20)) for j in range(10)] for i in range(20)]

    # update screen
    display.update(), time.Clock().tick(3)

    # delete full rows
    m = [[m[i], [0]*10][all(m[i])] for i in range(20)]

    # shape moves down constantly
    m, y = [[[m[i][j] > 0, -1][c[r % len(s)][i-y][j-x]] for j in range(10)] for i in range(20)], [y+1, y][y > 16]

    # sleep(1)
    # m = [[m[i], [0]*10][all(m[i])] for i in range(20)]  # delete full rows # probably not needed anymore
    m = (20 - len(list(filter(lambda q: q != [1] * 10, m)))) * [[0] * 10] + list(filter(lambda q: q != [1] * 10, m))
    m = (20 - len([*filter(lambda q: ~all(q), m)])) * [[0] * 10] + [*filter(lambda q: ~all(q), m)]

"""
Steps:
    Shape should be represented with -1 or 2 on the map
    Gravity for already fallen items, which ignores the current shape
    Gravity for the shape, that keeps it together
    Movement left right for shape  | same operation, but on two lines because it accesses
    Rotation for shape             | the event getter 
    When shape reaches final point, make it into "already fallen item(s)"
    
    -------
    Ideas:
        - left, middle and right arrow for movement (or keys with consecutive ASCII codes)
"""
