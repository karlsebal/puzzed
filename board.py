#!/usr/bin/python3 -i
# vi: ai expandtab ts=4 sw=4 sts=4
"""
This is the board. It holds all tiles, positions and logic for put/remove.

The logic implemented here is rudimental: It only performs out-ouf-board
and collision testing.
"""

board = [ ['x' for i in range(8)] for j in range(8)]


class OccupiedException(Exception):
    """raised when tile cannot be put due to collision"""
    pass

class XOutRangeException(Exception):
    """raised when tile cannot be put due to x-out-of-bound"""
    pass

class YOutRangeException(Exception):
    """raised when tile cannot be put due to y-out-of-bound"""
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
    """puts a tile to (x,y) or removes it. Raise Exception if occupied or outbound."""

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
