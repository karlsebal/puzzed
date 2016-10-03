#!/usr/bin/python3 -i
# vi: ai expandtab ts=4 sw=4
""" provides permutation tree and basic operations"""

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


def permutate(tile):
    """return all permutations of tile including tile"""

    permutation = [tile,]

    # rotations 1 to 3 are the actual rotations
    for i in range(3):
         permutation.append(rotate(permutation[i]))

    # and flipper not to forget
    permutation.append(flip(tile))

    # rotations for flipper
    for i in range(4,7):
        permutation.append(rotate(permutation[i]))

    return permutation
     

def equals(tile1, tile2):
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


def deduplicate(permutation):
    """deduplicate a permutation"""

    deduped = []

    # check tiles in the permutation
    for tile in permutation:
        duplicate = False

        # look if its already there
        for dtile in deduped:
            if equals(dtile, tile):
                duplicate = True

        if not duplicate:
            deduped.append(tile)

    return deduped


def deduplicated_permutation(tile):
    """return a list of deduplicated permutation including tile"""
    return deduplicate(permutate(tile))


def getAllPermutations():
    """returns a list with all permutation. one permutation of a tile per line."""
    
    all_permutations = []

    for ptile in tiles:
        tile_permutation = []

        for dtile in deduplicated_permutation(ptile):
            tile_permutation.append(dtile)

        all_permutations.append(tile_permutation)

    return all_permutations

def printAllPermutations():
    """give a nice output"""
    
    count = 0

    for permutation in getAllPermutations():
        
        count += 1
        print('### Permutation Tile %d ###' % count)
        
        for tile in permutation:
            out(tile)
