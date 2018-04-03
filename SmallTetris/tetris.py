from pygame import *
from random import *

s = [[[[1, 1, 1, 1]], [[1], [1], [1], [1]]], [[[1, 1], [1, 1]]],
     [[[1], [1], [1, 1]], [[1, 1, 1], [1]], [[1, 1], [0, 1], [0, 1]]]]
m = [[0 for _ in range(10)] for _ in range(22)]
g, c = display.set_mode((300, 300)), s[randint(0, 3)]

while True:

    display.update()