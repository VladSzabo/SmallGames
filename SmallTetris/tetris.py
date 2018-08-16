from pygame import display as d, KEYUP as K, event as v, draw as p, time as t
from random import choice as k
e, o = (lambda: all([[1, m[i+1][j] != 1][m[i][j] < 0] for j in range(w) for i in range(h)])), (lambda q: [k(s), c][q])
b = (lambda: [i for i in m if ~all(i)+2], lambda z: [[c[j][i] for j in range(z)][::u]+c[i][z:] for i in range(z)]+c[z:])
s = [[[*map(int, bin(int(i))[:1:-1])]+[0]*20 for i in str(j)]+[[0]*20]*20 for j in [33, 2222, 630, 360, 113, 223, 720]]
m, g, c, x, y, w, h, u, i, j, cc = [[0]*10]*20, d.set_mode((200, 400)), k(s), 4, 0, 10, 20, -1, [[0]*10], [[1]*10], 255
while d.update() or t.Clock().tick(30):
    x, c = {0: [(x+1, c), (x-1, c), (x, b[1](len(c)-h))][e.key-275] for e in v.get() if e.type == K}.get(0) or (x, c)
    _, m = [p.rect(g, m[i][j]*cc, (j*h, i*h, h, h)) for j in range(w) for i in range(h)], (h-len(b[0]()))*i+b[0]()+j
    m, y, c = [[[m[i][j] > 0, [1, -1][e()]][c[i-int(y)][j-x]] for j in range(w)] for i in range(h)], e()*y+0.1, o(e())

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