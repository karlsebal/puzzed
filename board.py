#!/usr/bin/python3 -i
# vi: ai expandtab ts=4 sw=4 sts=4
"""
This is the board. It holds all tiles, positions and logic for put/remove.

The logic implemented here is rudimental: It does only out-ouf-board
and collision testing.
"""


from permutation import getAllPermutations as getAll
from permutation import printAllPermutations as printAll

## convenience

from permutation import tiles 
from permutation import out as tout

t = tiles[10]

def testpr(tile,timer=0.7):
    import time
    try:
        for y in range(8):
            try:
                for x in range(8):
                    try:
                        put(tile,x,y)
                        out()
                        put(tile,x,y,True)
                        time.sleep(timer)
                    except OccupiedException:   
                        pass

            except XOutRangeException:
                pass
    except YOutRangeException:
        pass


def test(tile, xoffset=0, yoffset=0, remove=False):
    putlist=[]
    try:
        for y in range(8):
            try:
                for x in range(8):
                    try:
                        put(tile,x+xoffset,y+yoffset,remove)
                        putlist.append((x,y))
                        out()
                    except OccupiedException:   
                        pass

            except XOutRangeException:
                pass
    except YOutRangeException:
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


board = [ ['x' for i in range(8)] for j in range(8)]


class OccupiedException(Exception):
    pass

class XOutRangeException(Exception):
    pass

class YOutRangeException(Exception):
    pass


def out() -> None:
    """gives a nice output of the board"""

    print()
    for row in board:
        for square in row:
            print(square if square != 'x' else '.', end='')
        print()
    print()


def clear() -> None:
    """clear board"""

    for x in range(len(board[0])):
        for y in range(len(board)):
            board[y][x] = 'x'


def remove(tile, topLeftX, topLeftY):
    """remove tile from (x,y). No checking."""

    put(tile, topLeftX, topLeftY, True)

    

def put(tile, topLeftX: int, topLeftY: int, remove=False) -> None:
    """puts a tile to (x,y). Raise Exception if occupied or outbound"""

    # get dimensions
    xDim = len(tile[0])
    yDim = len(tile)

    # TODO better outbound checking.
    # check if out of bound
    if xDim + topLeftX > len(board[0]):
        raise XOutRangeException

    if yDim + topLeftY > len(board):
        raise YOutRangeException

    # get range
    rangeX = range(topLeftX, topLeftX + xDim)
    rangeY = range(topLeftY, topLeftY + yDim)


    # we need counters to know
    # which square to compare
    countX = 0
    countY = 0


    # we check xyDim from position..
    if not remove:
        for x in rangeX:
            for y in rangeY:
                # if the square on the board is occupied ...
                if board[y][x] != 'x':
                    # ... the square on the tile must be empty.
                    if tile[countY][countX] != 'x':
                        # its not! 
                        raise OccupiedException
                countY += 1
            countY = 0
            countX += 1



    # check was okay, lets copy
    countX = 0
    countY = 0

    for x in rangeX:
        for y in rangeY:
            # put/remove square only if there..
            if tile[countY][countX] != 'x':
                board[y][x] = 'x' if remove else tile[countY][countX]

            countY += 1

        countY = 0
        countX += 1
