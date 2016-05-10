from colorama import *

from tile import TileType, Tile


class OutOfBoundsException(Exception):
    pass


class InvalidPlacementException(Exception):
    pass


class Space:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tile = TileType.NONE
        self.player = None


class Board:
    def __init__(self, width, height):
        self._board = []
        self._width = width
        self._height = height

        self._last_space = None

        # Initialize board spaces
        for x in range(width):
            row = []
            for y in range(height):
                row.append(Space(x, y))
            self._board.append(row)

    def get(self, x, y):
        if not self.is_in_bounds(x, y):
            raise OutOfBoundsException()

        return self._board[x][y]

    def place_piece(self, x, y, player, tile_type):
        if not self.is_placement_valid(x, y):
            raise InvalidPlacementException()

        space = self._board[x][y]
        space.tile = tile_type
        space.player = player
        self._last_space = space

    def clear_last(self):
        self._last_space = None

    def is_in_bounds(self, x, y):
        """ Returns True if the coord is a valid space on the board"""
        if 0 <= x < self._width:
            return True
        elif 0 <= y < self._height:
            return True
        return False

    def is_placement_valid(self, x, y):
        if not self.is_in_bounds(x, y):
            return False

        if self.get(x, y).tile != TileType.NONE:
            return False

        if self._last_space is None:
            return True

        last = self._last_space
        del_x = x - last.x
        del_y = y - last.y

        return Tile.is_placement_valid(last.tile, del_x, del_y)

    def any_valid_move(self):
        for x in range(self._width):
            for y in range(self._height):
                if self.is_placement_valid(x, y):
                    return True

        return False

    def print_board(self):

        color_reset = Fore.RESET + Back.RESET + Style.RESET_ALL

        for x in range(self._height):
            line = ''
            for y in range(self._width):
                space = self.get(x, y)
                symbol = Tile.tile_symbol(space.tile)

                if space.player:
                    color = space.player.color + Style.BRIGHT
                else:
                    color = color_reset

                line += '| ' + color + symbol + color_reset + ' '
            line += '|'
            print("-" * 17)
            print(line)
        print("-" * 17)

    def calculate_score(self, player):
        total = 0
        # Across
        for y in range(self._height):
            line = []
            for x in range(self._width):
                line.append(self.get(x, y))
            total += self._line_score(player, line)

        # Down
        for x in range(self._width):
            line = []
            for x in range(self._height):
                line.append(self.get(x, y))
            total += self._line_score(player, line)

        # Diagonal
        print("TODO: DIAGONAL SCORES")
        # TODO: this

        return total

    def _line_score(self, player, line):
        run = 0
        high_run = 0

        for space in line:
            if space.player == player:
                run += 1
                high_run = max(run, high_run)
            else:
                run = 0

        score = high_run - 2
        return max(score, 0)









