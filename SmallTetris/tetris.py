from pygame import display as d, KEYUP as K, event as v, draw as p, time as t
from random import randint as f
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

               464 -> 111010000

    1) T-form: 111          001         000         100
               010  -90->   011 -90->   010 -90->   110
               000          001         111         100

               432
    
    2) O-form: 110          011         000         000
               110  -90->   011 -90->   011 -90->   110
               000          000         011         110
    
    
               294
    
    3) L-form: 100          111         011         000
               100  -90->   100 -90->   001 -90->   001
               110          000         001         111
               
               150
               
    4) J-form: 010          100         011         000
               010  -90->   111 -90->   010 -90->   111
               110          000         010         001
               
               487

    5) C-form: 111          
               100  -90->   
               111          
               
               146
               
    6) I-form: 010
               010
               010
               
               240

    7) S-form: 011
               110
               000
               
               408
               
    8) Z-form: 110
               011
               000
    
    
"""

print([[[*map(int, f"{bin(j)[2:]}")][i:i+3]for i in range(0, 9, 3)]for j in [464, 432, 294, 150, 487, 146, 240, 408]])
shape = [[1, 1, 1], [1, 0, 0], [1, 1, 1]]
rotated_shape_90 = [[shape[j][i] for j in range(3)][::-1] for i in range(3)]
rotated_shape_180 = [[rotated_shape_90[j][i] for j in range(3)][::-1] for i in range(3)]
rotated_shape_270 = [[rotated_shape_180[j][i] for j in range(3)][::-1] for i in range(3)]

for i in shape:
    print("".join(str(j) for j in i))
print()
for i in rotated_shape_90:
    print("".join(str(j) for j in i))
print()
for i in rotated_shape_180:
    print("".join(str(j) for j in i))
print()
for i in rotated_shape_270:
    print("".join(str(j) for j in i))


s = [[[i+[0]*20 for i in r]+[[0]*20]*20 for r in s] for s in loads(open("s").read())]
m = [[f(0, 0) for _ in range(10)] for i in range(20)]
m[f(0, 19)] = [1]*10
m[f(0, 19)] = [1]*10
g = d.set_mode((200, 400))
c, r = s[2], 0
x, y = 3, 0
b = (lambda q: ~all(q)+2,)

while True:
    # handle movement and rotation
    x, r = [[{1: (x+1, r), 2: (x-1, r), 0: (x, r+1)}.get(e.key-274) for e in v.get() if e.type == K]+[(x, r)]][0][0]

    # draw map
    [[p.rect(g, [0, 255][m[i][j]], (j*20, i*20, 20, 20)) for j in range(10)] for i in range(20)]

    # update screen
    d.update(), t.Clock().tick(30)

    # shape moves down constantly
    m, y = [[[m[i][j] > 0, -1][c[r % len(s)][i-int(y)][j-x]] for j in range(10)] for i in range(20)], [y+.1, y][y > 16]

    # move map down when full lines are present
    m = (20-len([*filter(b[0], m)]))*[[0]*10]+[*filter(b[0], m)]

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
