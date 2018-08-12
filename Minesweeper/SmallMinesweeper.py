from pygame import *
from random import *
s, c, im = display.set_mode((300, 300)), sample(range(100), 10), [image.load(str([9, i-10][i > 9])) for i in range(22)]
m, h = [*map(lambda x:sum([i//10-1 <= x//10 <= i//10+1 and i % 10-1 <= x % 10 <= i % 10+1 for i in c]), range(200))], 30
while True:
    m = [[m[i], [m[i], m[i]+10][10 in [m[i-1], m[i+1], m[i-10], m[i+10]]]][m[i] < 10] for i in range(100)] + [0] * 100
    m[sum([(lambda t:t[1]//h*10+t[0]//h+h)(mouse.get_pos()) for e in event.get() if e.type == MOUSEBUTTONDOWN])-h] += 10
    display.update(), [s.blit(im[m[i]], (i % 10*h, i//10*h)) for i in range(100)], s.blit(im[20], [0]*2) if any([
        m[i] > 9 for i in c]) else s.blit(im[21], [0]*2) if all([m[i] > 9 for i in range(100) if i not in c]) else 1
