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

s = loads(open("s").read())
m = [[randint(0, 1) for _ in range(10)] for _ in range(20)]
g = display.set_mode((200, 400))
c, r = choice(s), 0
x, y = 10, -1

while True:
    m = [[[m, m, m][e.key - 274] for e in event.get() if e.type == KEYUP]+[m]][0][0]
    [[draw.rect(g, [0, 255][m[i][j]], (j*20, i*20, 20, 20)) for j in range(10)] for i in range(20)]
    display.update(), time.Clock().tick(10)
    m = [[m[i], [0]*10][all(m[i])] for i in range(20)]  # delete full rows

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

m = [[[m1, m2, m3][e.key - 274] for e in event.get() if e.type == KEYUP]+[m]][0][0]

Explanation:
    - if you press nothing, m = m
    - if you press ARROW_DOWN, m = m1
    - if you press ARROW_RIGHT, m = m2
    - if you press ARROW_LEFT, m = m3
"""
