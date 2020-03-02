from vect_class import Vector
import pygame as pg
from pygame.locals import *
from pygame_draw import pyg_draw
from math import ceil, floor, sin, cos, pi, tau, tan

pd = pyg_draw(1)
w, h = pd.cen()
clo = pd.clock
arr = []

v = Vector([200, 0], [w, h])
v1 = Vector([0, 300], v.e)#[w, h])

a = v.copy()#.inv(0, ret=1)
a1 = v1.copy()#.inv(1, ret=1)

a1.move(v.s)
#a.move(a.e)
#a.link(s=v1.e)
#a1.link(s=a.e)

#a.inv(1)

an = v.ang()
vcs = [a, a1]  + [v, v1]
#print(vcs, [id(i) for i in vcs])

run = True -0
c = -1
while run:
    clo.tick(60)
    c += 1
    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
    
    for i in vcs:
        i.draw(pd, 3)
        pd.circ(i.s, 5)
        i.draw_arrow(pd)
    alp = an+c/50%tau
    #vcs[2].set_ang(-alp)
    #vcs[0].set_ang(-alp)
    #v1.set_abs(c/50%tau)#c/1000%pi*100+(-tau)**2
    #arr.append(vcs[2].pts()[1])
    for i in arr:
        pd.circ(i)
    pd.upd()
    pd.fill()