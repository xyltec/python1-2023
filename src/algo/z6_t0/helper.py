
from model import Fraction


def add(f1: Fraction, f2: Fraction) -> Fraction:
    a = f1.numer()
    b = f1.denom()
    c = f2.numer()
    d = f2.denom()
    return (a*d + c * b) / (b * d)
