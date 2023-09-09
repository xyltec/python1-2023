def how_many_moves(start: tuple[int, int], finish: tuple[int, int], max_dim: tuple[int, int]) -> int | None:
    reached = set([start])
    current_positions = set([start])

    moves = 0

    while finish not in reached:
        new_positions = set()

        # przejść przez wszystkie pozycje z current_positions
        # dla kazdej wygenerowac nowe poprawne pozycje i wrzucić do n_positions

        moves += 1
        current_positions = new_positions
        if moves > 2 * max(max_dim):
            return None

    return moves