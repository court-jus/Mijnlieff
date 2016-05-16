from enum import Enum


class InvalidTileTypeException(Exception):
    pass


class TileType(Enum):
    NONE = 0
    DIAG = 1
    LINE = 2
    PUSH = 3
    PULL = 4


class Tile:
    TYPES = [TileType.DIAG, TileType.LINE, TileType.PULL, TileType.PUSH]

    @staticmethod
    def is_valid_type(tile):
        return tile in Tile.TYPES

    @staticmethod
    def tile_symbol(tile):
        if tile == TileType.NONE:
            return ' '
        elif tile == TileType.DIAG:
            return 'X'
        elif tile == TileType.LINE:
            return '+'
        elif tile == TileType.PUSH:
            return 'O'
        elif tile == TileType.PULL:
            return '*'
        else:
            raise InvalidTileTypeException()

    @staticmethod
    def tile_from_symbol(symbol):
        for tile in Tile.TYPES:
            if symbol == Tile.tile_symbol(tile):
                return tile
        return TileType.NONE

    @staticmethod
    def is_placement_valid(last_tile_type, relative_x, relative_y):
        """ Determine if a new piece placed relative to the previous piece of a known type
        is valid. Does NOT check if the new piece would fall within the bounds of the board.

        :param last_tile_type: The TileType of the last tile
        :param relative_x: The x coordinate of the new piece relative to that of the previous piece
        :param relative_y: The y coordinate of the new piece relative to that of the previous piece
        """
        tile = last_tile_type
        x = relative_x
        y = relative_y

        if x == 0 and y == 0:
            return False

        if tile == TileType.NONE:
            return True

        elif tile == TileType.DIAG:
            return abs(x) == abs(y)

        elif tile == TileType.LINE:
            return x == 0 or y == 0

        elif tile == TileType.PUSH:
            return abs(x) > 1 and abs(y) > 1

        elif tile == TileType.PULL:
            return abs(x) in [0, 1] and abs(y) in [0, 1]

        else:
            raise InvalidTileTypeException()
