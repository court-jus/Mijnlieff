from colorama import *

from board import Board
from player import Player

class MijnlieffGame:
    def __init__(self):
        self.board = Board(4, 4)

        self._p1 = Player("Player 1", Fore.RED)
        self._p2 = Player("Player 2", Fore.BLUE)

        self._next_player = self._p1

    def next_player(self):
        return self._next_player

    def _switch_player(self):
        if self._next_player == self._p1:
            self._next_player = self._p2
        else:
            self._next_player = self._p1

    def place_piece(self, x, y, player, tile_type):
        if not player.has_tile(tile_type):
            print("Player has no more tiles of that type remaining")
            return False
        elif not self.board.is_in_bounds(x, y):
            print("Selected space is outside the board bounds")
            return False
        elif not self.board.is_placement_valid(x, y):
            print("Piece placement is invalid")
            return False

        self.board.place_piece(x, y, player, tile_type)
        player.place_tile(tile_type)

        # Check if game is over
        if self.is_over():
            p1_score = self.board.calculate_score(self._p1)
            p2_score = self.board.calculate_score(self._p2)
            print("Game over - " + self._p1.name() + " - " + str(p1_score) + " pts; "
                  + self._p2.name() + " - " + str(p2_score) + " pts")

        # Check that the next player is allowed to move
        if self.board.any_valid_move():
            self._switch_player()
        else:
            self.board.clear_last()

        return True

    def print_board(self):
        self.board.print_board()

    def is_over(self):
        return not self._p1.has_any_tile() or not self._p2.has_any_tile()