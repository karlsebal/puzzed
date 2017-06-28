#!/usr/bin/python3 -i
# vi: ai expandtab sts=4 ts=4 sw=4

import board

import logging

log = logging.getLogger(__name__)

class Board_Controller:
    """
    This is the board controller. She is aware of tiles and positions.
    """

    def __init__(self, board: board.Board):
        self.board = board
        self.index = []

    def put(tile):
        """
        Add tile and insert into first possible position.
        Return index and coordinates if successfull, 
        Raise Exception otherwise
        """
        
        raise Exception('NIY')


    def move(tile_index: int):
        """
        move tile with index <tile_index> to next possible position.
        Return coordinates if successful,
        Raise Exception otherwise
        """

        raise Exception('niy')

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




