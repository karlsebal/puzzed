#!/usr/bin/python3 -i
# vi: ai expandtab ts=4 sw=4 sts=4
"""provides permutation tree"""

from data import tiles

from tile import permutate
from tile import to_string

import board as board_module
from board import OccupiedException, YOutRangeException, XOutRangeException

from board_controller import Board_Controller

import logging

log = logging.getLogger(__name__)

ddebug = False
log_level = logging.INFO

logging.basicConfig(level=log_level,
                    format='%(asctime)s – ' +
                            ('%(funcName)s in ' if ddebug else '') +
                            ' %(module)s – %(levelname)s: %(message)s')


# create a new board and controller
board = board_module.Board(8, 8)
controller = Board_Controller(board)

# get all permutations
permutations = []

for tile in tiles:
    permutations.append(permutate(tile))

### TESTING ###

import time

board.put_tile(tiles[5], 2, 2)

for permutation in permutations:

    for tile in permutation:
        try:

            for j in range(board.y_dim):
                try:
                    for i in range(board.x_dim):
                        try:
                            log.debug('put tile to %d,%d' % (i,j))
                            board.put_tile(tile, i, j)
                            print(board)
                            time.sleep(.2)
                            log.debug('remove tile from %d,%d' % (i,j))
                            board.remove_tile(tile, i, j)
                        except OccupiedException:
                            log.debug('%d,%d occupied' % (i,j))

                except XOutRangeException:
                        log.debug('%d,%d xout' % (i,j))

        except YOutRangeException:
                    log.debug('%d,%d yout' %(i,j))
                    


