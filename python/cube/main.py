import sys
import time

w, h, out = 80, 24, sys.stdout

cube = [
    (x, y, z) 
    for x in -1, 1 for y in -1, 1 for z in -1, 1
]

s = 0.1                                 # sine
c = (1 - s**2)**0.5                     # cosine
ym = h/3                                # Y magnification
xm = 2*ym                               # X magnification

while True:
    cube = [(c*x + s*z, y, -s*x + c*z) for x, y, z in cube] # Rotate by theta.
    proj = [(round(w/2+xm*x/(z+2)), round(h/2+ym*y/(z+2))) for x, y, z in cube]
    out.write('\033[H' + '\n'.join(
            ''.join(('*' if (x, y) in proj else ' ') for x in range(w))
            for y in range(h)))
    out.flush()
    time.sleep(1/15.0)