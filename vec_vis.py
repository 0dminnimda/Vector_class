from vect_class import Vector
import pygame as pg
from pygame.locals import *
from pygame_draw import pyg_draw
from math import ceil, floor, sin, cos, pi, tau, tan

pd = pyg_draw(1)
w, h = pd.cen()
clo = pd.clock
v = Vector([200, 0], [w, h])
v1 = Vector([0, 300], v.e)#[w, h])
v2 = Vector([200, 100], v1.e)#[w, h])
v3 = Vector([300, 200], v2.e)
#v2 = v - v1

lin = lin2 = Vector([200, 0], [w, h])

#v1.perp(2.5)

#v1.inv()
#v3 = v1.inv(0, ret=True)
#v4 = v1.inv(1, ret=True)
#v5 = v1.perp([0, 0], ret=True)
#v1.inv(1)

su = v + v1 + v2 - v3
v3.inv(0, 1)

a = Vector(v.ptsv(), v1.e)
b = Vector(v1.ptsv(), v.e)

an = v.ang()
arr = []
vcs = [lin, lin2]#v, v1, v2, v3, su]
lin.link(v)
print(id(v), id(lin.link))

run = True
c = -1
while run:
    clo.tick(60)
    c += 1
    for event in pg.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                run = False
    
    #vcs[2] = vcs[0] + vcs[1]
    for i in vcs:
        i.draw(pd, 3)
    alp = an+c/50%tau
    vcs[0].set_ang(-alp)
    #vcs[2].set_ang(-alp)
    #vcs[2].set_ang(alp)
    #v1.set_abs(c/50%tau)#c/1000%pi*100+(-tau)**2
    #arr.append(vcs[2].pts()[1])
    for i in arr:
        pd.circ(i)
    pd.upd()
    pd.fill()