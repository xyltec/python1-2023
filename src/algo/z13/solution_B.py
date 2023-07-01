def get_area(x1, y1, x2, y2) -> int:
    szerokosc = abs(x2 - x1) + 1
    wysokosc = abs(y2 - y1) + 1

    return szerokosc * wysokosc