#!/usr/bin/python3 -i
# vi: ai expandtab ts=4 sw=4 sts=4
"""provides permutation tree"""

from data import tiles

from tile import permutate
from tile import to_string

from board import Board
from board import OccupiedException, YOutRangeException, XOutRangeException

from board_controller import Board_Controller
from board_controller import NoMoveLeft

import logging

log = logging.getLogger(__name__)

ddebug = True
log_level = logging.INFO

logging.basicConfig(level=log_level,
                    format='%(asctime)s – ' +
                            ('%(funcName)s in ' if ddebug else '') +
                            ' %(module)s – %(levelname)s: %(message)s')


# create a new board and controller
controller = Board_Controller(Board(8,8))

# get all permutations
permutations = []

for tile in tiles:
    permutations.append(permutate(tile))

### TESTING ###

import time

controller.board.put_tile(tiles[5], 2, 2)
print(controller.board)


for permutation in permutations:

    for tile in permutation:
        try:
            idx = controller.put(tile)
            print(controller.board)

            while True:
                coordinates = controller.move(idx)
                print(controller.board)
                time.sleep(.025)

        except NoMoveLeft as e:
            pass
