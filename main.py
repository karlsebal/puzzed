#!/usr/bin/python3 -iu
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

from chess_board_controller import ChessBoardController
from chess_board_controller import NoMoveLeft

import logging

log = logging.getLogger(__name__)

ddebug = False
log_level = logging.INFO

recursion_info_level = 8

logging.basicConfig(level=log_level,
                    format='%(asctime)s – ' +
                            ('%(funcName)s in ' if ddebug else '') +
                            ' %(module)s – %(levelname)s: %(message)s')


# create a new board and controller
controller = ChessBoardController(ChessBoard())

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

def try_all_moves(index: int=None) :
    """
    recursively try all moves of all permutations in
    permutations on controller

    The function is meant to be called without a parameter,
    figuring out the size of permutations and doing all
    subsequent calls. 
    So index is also kind of an init-flag
    """
    permutation_count = 0
    permutations_count = len(permutations[index]) if index else None

    log.debug('recursion level %r' % index)

    # init
    if index == None:
        try_all_moves(len(permutations) - 1)

    # if index is defined already
    # and the end of depth is reached,
    # we have a solution
    elif index == -1:
        
        solutions.append(controller.get_solution())
        solutions.append(str(controller.board))
        print('SOLUTION')
        print(solutions[-1])
        print('all')
        print(solutions)

    # if not we are somewhere in the search tree
    else:
        # for every tile in the specific permutation…
        for tile in permutations[index]:
            permutation_count += 1
            move_count = 0

            # feedback
            if not index < recursion_info_level:
                log.info('permutation %d/%d@%d' % (permutation_count, permutations_count, index))

            try:
                # …we try to put that tile on board…
                log.debug('put %r' % tile)  
                idx = controller.put(tile)
                log.debug('%r is index %d' % (tile, idx))

                # feedback
                move_count += 1
                if not index < recursion_info_level:
                    log.info('move %d@%d(%d/%d)' % (move_count, index, permutation_count, permutations_count))
                    log.info('\n' + str(controller.board))
                # TODO trigger event time.sleep(DELAY)

                # …descend the tree…
                log.debug('next recursion level…')
                try_all_moves(index - 1)

                while True:
                    # …and as we come back move it around…
                    log.debug('move %d' % idx)
                    coordinates = controller.move(idx)
                    log.debug('%d now on %r' % (idx, coordinates))

                    # feedback
                    move_count += 1
                    if not index < recursion_info_level:
                        log.info('move %d@%d(%d/%d)' % (move_count, index, permutation_count, permutations_count))
                        log.info('\n' + str(controller.board))
                    # TODO trigger event time.sleep(DELAY)

                    # …and descend
                    log.debug('next recursion level…')
                    try_all_moves(index -1)

            except NoMoveLeft:
                log.debug('no move left for %r' % tile)


if __name__ == "__main__":
    try_all_moves()
    print(solutions)
