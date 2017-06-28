#!/usr/bin/python3 -i
# vi: ai expandtab sts=4 ts=4 sw=4

def to_string(tile):
    string = ''
    for line in tile:
        for square in line:
            string += str(square)
        string += '\n'
    # remove trailing LF
    return string[0:-1]

    
def rotate(tile):
    """return 90° rotated tile."""

    ## x is width and y is hight
    # x is len of row
    x = len(tile[0])

    # y is len of tile
    y = len(tile)

    # y is read backwards, x forwards
    x_range = range(x)
    y_range = range(y-1, -1, -1)

    return [ [tile[y][x] for y in y_range] for x in x_range]


def flip(tile):
    """flip tile over y axis. return tile."""

    return [ [square for square in reversed(row)] for row in tile]


def permutate(tile) -> list:
    """return permutations of tile including the tile herself"""

    permutation = []
    tile_store = tile

    # function for deduped add
    def add(tile):
        """add the tile if not already in"""
        if tile not in permutation:
            permutation.append(tile)


    # first one is the tile itself.
    permutation.append(tile)

    # rotations 1 to 3 are the actual rotations
    # always the 'previous' rotation is rotated..
    for i in range(3):
        tile_store = rotate(tile_store)
        add(tile_store)

    # flipper. flip the original
    tile_store = flip(tile)
    add(tile_store)

    # rotations for flipper
    for i in range(4,7):
        tile_store = rotate(tile_store)
        add(tile_store)

    return permutation


def equals(tile1, tile2) -> bool:
    """compare to tile. return True if equal False otherwise"""

    # compare y dim
    if len(tile1) != len(tile2):
        return False

    # compare x dim
    if len(tile1[0]) != len(tile2[0]):
        return False

    # compare square by square
    for i in range(len(tile1)):
        for j in range(len(tile1[0])):
            if tile1[i][j] != tile2[i][j]:
                return False

    return True
