#!/usr/bin/python3 -i
# vi: ai expandtab ts=4 sw=4 sts=4
"""provides permutation tree and basic tile operations"""

from tiles import tiles

def out(tile):
    """output tile"""

    print()
    for row in tile:
        for square in row:
            if not square:
                print('N', end='')
            elif square == 'x':
                print('.', end='')
            else:
                print(square, end='')

        print()
    print()


def rotate(tile):
    """rotates 90° right. returns tile."""

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
    """return permutations of tile"""

    permutation = []

    # function for deduped add
    def add(tile):
        """add the tile if not already in"""
        if tile not in permutation:
            permutation.append(rotation)


    # first one is the tile itself.
    permutation.append(tile)

    # rotations 1 to 3 are the actual rotations
    # always the 'previous' rotation is rotated..
    rotation = tile

    for i in range(3):
        rotation = rotate(rotation)
        add(rotation)

    # flipper. put it in rotation though
    rotation = flip(tile)
    add(rotation)

    # rotations for flipper
    for i in range(4,7):
        rotation = rotate(rotation)
        add(rotation)


    return permutation
     

def equals(tile1, tile2) -> bool:
    """compare tiles. return True if equal False otherwise"""

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


def getAllPermutations() -> list:
    """returns a list with all permutation. one permutation of a tile per line."""
    
    permutations = []

    for tile in tiles:
        permutations.append(permutate(tile))

    return permutations
        


def printAllPermutations() -> None:
    """give a nice output"""
    
    count = 0

    for permutation in getAllPermutations():
        
        count += 1
        print('### Permutation Tile %d ###' % count)
        
        for tile in permutation:
            out(tile)
