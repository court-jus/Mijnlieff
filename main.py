from tile import TileType, Tile
from game import MijnlieffGame


game = MijnlieffGame()

while not game.is_over():
    game.print_board()
    player = game.next_player()

    print(player.name() + " tiles: " + player.list_tiles())

    tile = TileType.NONE
    while not Tile.is_valid_type(tile):
        symbol = input(player.name() + " select tile type: ")
        tile = Tile.tile_from_symbol(symbol)

        if tile == TileType.NONE:
            print("Invalid tile type")
        if not player.has_tile(tile):
            print("Player has no more tiles of that type remaining")
            tile = TileType.NONE

    move_ok = False
    while not move_ok:
        move = input(player.name() + " select location for '" + Tile.tile_symbol(tile) + "': ")
        try:
            x, y = [int(i) for i in move.split(" ")]
        except ValueError:
            print("Invalid location")
            continue

        move_ok = game.place_piece(x, y, player, tile)





