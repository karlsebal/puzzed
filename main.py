#!/usr/bin/python3 -i
# vi: ai expandtab ts=4 sw=4 sts=4
"""
search controller. 

gets all permutations, which is the search matrix and recuresively
tries them
"""

from data import tiles

from tile import permutate
from tile import to_string

from board import ChessBoard
from board import OccupiedException, YOutRangeException, XOutRangeException

from board_controller import Board_Controller
from board_controller import NoMoveLeft

import logging

log = logging.getLogger(__name__)

ddebug = False
log_level = logging.INFO

logging.basicConfig(level=log_level,
                    format='%(asctime)s – ' +
                            ('%(funcName)s in ' if ddebug else '') +
                            ' %(module)s – %(levelname)s: %(message)s')


# create a new board and controller
controller = Board_Controller(ChessBoard())

# get all permutations
# this will be the search matrix
permutations = []

for tile in tiles:
    permutations.append(permutate(tile))

for permutation in permutations:
    log.debug('###')
    log.debug(permutation)
    for tile in permutation:
        log.debug('***')
        log.debug(tile)

# declare solutions
solutions = []

# TODO trigger event
import time
DELAY = 0

def try_all_moves(index: int=None) :
    """
    recursively try all moves of all permutations in
    permutations on controller

    The function is meant to be called without a parameter,
    figuring out the size of permutations and doing all
    subsequent calls. 
    So index is also kind of an init-flag
    """

    log.debug('recursion level %r' % index)

    # if index is defined already…
    # …and the end of depth is reached,
    # we have a solution
    if index and index == -1:
        solutions.append(controller.get_solution())
        print('SOLUTION')
        print(solutions[-1])

    # …and end of depth is not reached
    elif index and index > -1:
        # for every tile in the specific permutation
        for tile in permutations[index]:

            try:
                # we try to put that tile on board…
                log.debug('put %r' % tile)  
                idx = controller.put(tile)
                log.debug('%r is index %d' % (tile, idx))
                print(controller.board)
                time.sleep(DELAY)

                # …call the next instance…
                log.debug('next recursion level…')
                try_all_moves(index - 1)
                while True:
                    # …and move it around…
                    log.debug('move %d' % idx)
                    coordinates = controller.move(idx)
                    log.debug('%d now on %r' % (idx, coordinates))
                    print(controller.board)
                    time.sleep(DELAY)
                    # …while calling
                    log.debug('next recursion level…')
                    try_all_moves(index -1)

            except NoMoveLeft:
                log.debug('no move left for %r' % tile)

    # init
    elif not index:
        try_all_moves(len(permutations) - 1)

if __name__ == "__main__":
    try_all_moves()
    print(solutions)
