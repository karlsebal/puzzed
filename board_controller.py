#!/usr/bin/python3 -i
# vi: ai expandtab sts=4 ts=4 sw=4

from board import Board
from board import OccupiedException, XOutRangeException, YOutRangeException

import logging

log = logging.getLogger(__name__)

class NoMoveLeft(Exception):
    pass

class Board_Controller:
    """
    This is the board controller. She is aware of tiles and positions.
    """

    def __init__(self, board: Board):
        self.board = board
        self.index = []

    def put(self, tile):
        """
        Add tile and insert into first possible position.
        Return index if successfull, 
        Raise Exception otherwise
        No artifacts.
        """

        log.debug('put %r' % tile)

        try:
            # one more to provoke exception
            for j in range(self.board.y_dim + 1):
                try:
                    for i in range(self.board.x_dim):
                        try:
                            log.debug('try put at %d,%d' % (i,j))
                            self.board.put_tile(tile, i, j)
                            self.index.append([i, j, tile])
                            return len(self.index) - 1
                        except OccupiedException:
                            log.debug('%d, %d occupied' % (i,j))

                except XOutRangeException:
                        log.debug('%d, %d xout' % (i,j))
        except YOutRangeException:
            log.debug('%d, %d yout' % (i, j))
            raise NoMoveLeft

        log.error('FATAL')



    def move(self, tile_index: int):
        """
        move tile with index <tile_index> to next possible position.
        Return coordinates if successful,
        Raise Exception otherwise
        No artifacts. When final margin is hit board is left clean.
        """

        current_x = self.index[tile_index][0] 
        current_y = self.index[tile_index][1] 
        current_t = self.index[tile_index][2]

        log.debug('tile is at %d,%d – removing' % (current_x, current_y))
        self.board.remove_tile(current_t, current_x, current_y)

        # we can leave this when once set for i has to start at 0 then everytime
        wasXOut = False

        try:
            for j in range(self.index[tile_index][1], self.board.y_dim):
                log.debug('j is %d' % j)

                try:
                    for i in range(self.index[tile_index][0] + 1 if not wasXOut else 0, self.board.x_dim):
                        log.debug('i is %d' % i)

                        try:
                            log.debug('try putting to %d,%d' % (i,j))
                            self.board.put_tile(current_t, i, j)
                            self.index[tile_index][0] = i
                            self.index[tile_index][1] = j
                            return (i,j)
                        except OccupiedException:
                            log.debug('%d,%d occupied' % (i,j))

                except XOutRangeException:
                    log.debug('%d,%d xout' % (i,j))
                    wasXOut = True

        except YOutRangeException:
            log.debug('%d,%d yout' % (i,j))


        raise NoMoveLeft


    def get_solution():
        """
        return the solution in its current state
        """

        return self.index

    def get_pretty_solution():
        """
        return pretty solution string
        """

        raise Exception('niy')
