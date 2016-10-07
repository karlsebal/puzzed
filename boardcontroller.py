#!/usr/bin/python3 -i
# vi: ai expandtab ts=4 sw=4 sts=4
"""
The BoardController

    TODO
She should hold a table with positions of tiles
so provide put and remove and maybe move, next a.s.f.
should be able to validate chess matrix (bwbw)
(should at some time be able to handle doubles of tiles)
"""


## convenience

from board import put
from board import remove
from board import out
from board import clear
from board import XOutRangeException
from board import YOutRangeException
from board import OccupiedException

from permutation import getAllPermutations as getAll
from permutation import printAllPermutations as printAll


from permutation import tiles 
from permutation import out as tout

t = tiles[10]

def test(tile, xoffset=0, yoffset=0, remove=False):
    putlist=[]
    try:
        for x in range(7):
            try:
                for y in range(7):
                    try:
                        put(tile,x+xoffset,y+yoffset,remove)
                        putlist.append((x,y))
                        out()
                    except OccupiedException:
                        pass
            except YOutRangeException:
                pass
    except XOutRangeException:
        pass
    

    return putlist

def putremove(tile):
    l = test(tile)
    for i in l:
        remove(tile, i[0], i[1])
        out()

def putremoveall(t):
    for t in tiles:
        putremove(t)

## /convenience
