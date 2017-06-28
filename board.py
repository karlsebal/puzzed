#!/usr/bin/python3 -i
# vi: ai expandtab ts=4 sw=4 sts=4
"""
Board class and exceptions
"""

class OccupiedException(Exception):
    pass

class XOutRangeException(Exception):
    pass

class YOutRangeException(Exception):
    pass

class Board:
    """
    This is the board. It holds all squares but is unaware of the tiles.

    The logic implemented here for put/remove is rudimental: 
    It does only out-ouf-board and collision testing.
    """

    def __init__(self, x_dim, y_dim):
        self.board = [ ['x' for i in range(x_dim)] for j in range(y_dim)]
        self.x_dim = x_dim
        self.y_dim = y_dim


    def __str__(self):
        out=''
        for row in self.board:
            for square in row:
                out+=square if square != 'x' else '.'
            out+='\n'
        return out


    def clear_board(self) -> None:
        """clear board"""

        for x in range(len(self.board[0])):
            for y in range(len(self.board)):
                self.board[y][x] = 'x'


    def remove_tile(self, tile, topLeftX, topLeftY) -> None:
        """remove tile from (x,y). No checking."""

        self.put_tile(tile, topLeftX, topLeftY, True)

        

    def put_tile(self, tile, topLeftX: int, topLeftY: int, remove=False) -> None:
        """puts a tile to (x,y). Put empty squares if removal requested. Raise Exception if occupied or outbound"""
        # TODO validator

        # get dimensions
        xDim = len(tile[0])
        yDim = len(tile)

        # TODO better outbound checking.
        # TODO merge with occupied check?
        # check if out of bound
        if xDim + topLeftX > len(self.board[0]):
            raise XOutRangeException

        if yDim + topLeftY > len(self.board):
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
                    if self.board[y][x] != 'x':
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
                    self.board[y][x] = 'x' if remove else tile[countY][countX]

                countY += 1

            countY = 0
            countX += 1
