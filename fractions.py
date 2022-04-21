
"""
Seite 181, Aufgabe 3.5
"""


class Fraction:

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        if denominator == 0:
            raise ZeroDivisionError("Nenner darf nicht 0 sein!")

    # Vorzeichen (Minus)
    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    # Addition
    def __add__(self, other):
        other = self._validate_other(other)
        lcm = self.lcm(self.denominator, other.denominator)
        f1, f2 = (f.expand(lcm // f.denominator) for f in (self, other))
        assert f1.denominator == f2.denominator, "denominators must be equal"
        return self.__class__(
                numerator=f1.numerator + f2.numerator,
                denominator=f1.denominator
            ).shorten()

    # Subtraktion
    def __sub__(self, other):
        other = self._validate_other(other)
        return self + (-other)

    # Multiplikation
    def __mul__(self, other):
        other = self._validate_other(other)
        return self.__class__(numerator=self.numerator * other.numerator,
                             denominator=self.denominator * other.denominator).shorten()
        
    # Division
    def __truediv__(self, other):
        other = self._validate_other(other)
        other = self.__class__(other.denominator, other.numerator)
        return self.__mul__(other)
    
    # Vergleichsoperationen
    def __eq__(self, other):
        if type(other) == Fraction:
            return self.decimal() == other.decimal()
        return self.decimal() == other

    def __lt__(self, other):
        if type(other) == Fraction:
            return self.decimal() < other.decimal()
        return self.decimal() < other

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        if type(other) == Fraction:
            return self.decimal() > other.decimal()
        return self.decimal() > other

    def __ge__(self, other):
        return self == other or self > other
    
    # Dezimalwert
    def decimal(self):
        return self.numerator / self.denominator

    # Ausgabe
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    def __repr__(self): return self.__str__()
    
    @classmethod
    def gcd(cls, a, b):
        while b: a,b = b, a%b
        return a
    
    @classmethod
    def lcm(cls, a, b):
        return abs(a * b) // cls.gcd(a, b)
    
    def shorten(self):
        """simplifies the fraction (in-place method)"""
        gcd = self.gcd(self.numerator, self.denominator)
        self.numerator //= gcd
        self.denominator //= gcd
        return self

    def expand(self, factor):
        return self.__class__(
            self.numerator * factor,
            self.denominator * factor)
        
    @classmethod
    def scalar_to_fraction(cls, scalar):
        if type(scalar) is not int:
            raise TypeError("scalar must be an int")
        return cls(numerator=scalar, denominator=1)

    def _validate_other(self, other):
        if type(other) is int:
            other = self.scalar_to_fraction(other)
        elif type(other) is not self.__class__:
            raise TypeError("the argument must be type: Fraction OR int")
        return other


######################################################################
# TEST
f = Fraction(numerator=9, denominator=45)
print(f)
f.shorten()
print(f)


f1 = Fraction(9, 18)
f2 = Fraction(3, 8)
print(f1 / f2)


# TEST
from operator import add, sub, mul, truediv
from random import randint

for op in (add, sub, mul, truediv):
    print(f"\ttesting {op.__name__}...")
    for _ in range(100):
        a,b,c,d = sorted(randint(1, 1000) for _ in "....")
        f1, f2 = (Fraction(x,y).shorten() for x,y in [(a,b), (c,d)])
        
        d = op(f1.decimal(), f2.decimal())
        f3 = op(f1, f2)
        d3 = f3.decimal()
        
        if 0.9999 > d/d3 > 1.00001:
            print("ERROR", d, d3)
            raise Exception("!!")
        print(round(d3, 5) == round(d,5))





