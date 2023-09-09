"""
   :param position: position of a piece on the chessboard 
   :param max_dim: max dimensions of the board
   :return: True if the piece is on the board
"""
def is_on_board(position: tuple[int, int], max_dim: tuple[int, int] = (8, 8)):
    return (position[0] >= 0 and position[0] < max_dim[0]) and (position[1] >= 0 and position[1] < max_dim[1])
