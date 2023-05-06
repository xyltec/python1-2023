
from model import Fraction


def add(f1: Fraction, f2: Fraction) -> Fraction:
    a = f1.get_numer()
    b = f1.get_denom()
    c = f2.get_numer()
    d = f2.get_denom()
    numer = a * d + c * b
    denom = b * d
    return Fraction(numer, denom)
