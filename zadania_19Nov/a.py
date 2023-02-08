w = [1, 2, 3, 5]


def compute_diffs(w: list[int]) -> list[int]:
    diffs = []
    for idx in range(len(w) - 1):
        diffs.append(w[idx + 1] - w[idx])
    return diffs
