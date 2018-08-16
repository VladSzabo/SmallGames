from pygame import display as d, KEYUP as K, event as v, draw as p, time as t
from random import choice as k

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

               464 -> 111010000
                              
    Have the base.
    Make a lambda that rotates it once and expands it by 20x20
    
"""
e, o = (lambda: all([[1, m[i+1][j] != 1][m[i][j] < 0] for j in range(10) for i in range(20)])), (lambda q: [k(s), c][q])

b = (lambda q: ~all(q)+2, lambda z: [[c[j][i] for j in range(z)][::-1]+c[i][z:] for i in range(z)]+c[z:])
s = [[[*map(int, bin(int(i))[:1:-1])]+[0]*20 for i in str(j)]+[[0]*20]*20 for j in [33, 2222, 630, 360, 113, 223, 720]]
m, g, c, x, y = [[0 for _ in range(10)] for i in range(20)], d.set_mode((200, 400)), k(s), 4, 0

m[16:] = [[0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 1, 1, 0, 1, 1, 0, 0, 0, 0],
          [1, 1, 1, 1, 1, 1, 1, 0, 0, 0]]

while True:
    # handle movement and rotation
    x, c = {0: [(x+1, c), (x-1, c), (x, b[1](len(c)-20))][e.key-275] for e in v.get() if e.type == K}.get(0)or(x, c)

    # draw map
    [p.rect(g, m[i][j]*255, (j*20, i*20, 20, 20)) for j in range(10) for i in range(20)]

    # update screen
    d.update(), t.Clock().tick(30)

    # move map down when full lines are present
    m = (20-len([*filter(b[0], m)]))*[[0]*10]+[*filter(b[0], m)]+[[1]*10]

    # shape moves down constantly
    m, y, c = [[[m[i][j] > 0, [1, -1][e()]][c[i-int(y)][j-x]] for j in range(10)] for i in range(20)], e()*y+0.1, o(e())

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
