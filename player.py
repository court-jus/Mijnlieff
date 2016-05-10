from colorama import *

from tile import Tile


class InvalidPlayerNumberException(Exception):
    pass


class OutOfTilesException(Exception):
    pass


class Player:

    NUM_TILES = 1
    COLOR_RESET = Fore.RESET + Back.RESET + Style.RESET_ALL

    def __init__(self, name, color):
        self._name = name
        self.color = color
        self._tiles = {t: Player.NUM_TILES for t in Tile.TYPES}

    def name(self):
        return self.color + self._name + Player.COLOR_RESET

    def has_tile(self, tile_type):
        return self.remaining_tile_count(tile_type) > 0

    def has_any_tile(self):
        counts = [value for value in self._tiles.values()]
        return sum(counts) > 0

    def remaining_tile_count(self, tile_type):
        return self._tiles[tile_type]

    def place_tile(self, tile_type):
        if self.remaining_tile_count(tile_type) <= 0:
            raise OutOfTilesException()

        self._tiles[tile_type] -= 1

    def list_tiles(self):
        line = ''
        for tile in Tile.TYPES:
            if self.has_tile(tile):
                line += Tile.tile_symbol(tile) + "(" + str(self.remaining_tile_count(tile)) + "), "

        return line






