from dataclasses import dataclass


@dataclass
class Fraction:
    # ułamek = numer / denom
    numer: int
    denom: int

    def value(self):
        return self.numer / self.denom
    def numer(self):
        return self.numer
    def denom(self):
        return self.denom 

if __name__ == '__main__':
    f = Fraction(1, 2)
    assert f.value() == 0.5
