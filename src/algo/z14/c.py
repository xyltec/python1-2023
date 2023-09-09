from a import is_on_board
from b import make_move

valid_moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
def gen_new_positions(position: tuple[int,int], max_dim: tuple[int,int]) -> list[tuple[int,int]]:
    valid_positions = []
    for move in valid_moves:
        new_pos = make_move(position,move)
        if is_on_board(new_pos, max_dim):
            valid_positions.append(new_pos)
    return valid_positions
