# Creating a Fraction class from Chapter 1 of the text


class Fraction:
    """A class to act as data type:fraction"""

    def __init__(self, top, bottom):
        """Ensures that the input values are integers and reduces fraction by default"""
        try:
            int(top)
        except ValueError:
            print("Numerator could not be converted to integer")
        else:
            top = int(top)

        try:
            int(bottom)
        except ValueError:
            print("Denominator could not be converted to integer")
        else:
            bottom = int(bottom)

        # Ensuring that the denominator is a non-negative number
        if bottom < 0:
            bottom *= -1

        common = gcd(top, bottom)
        self.num = top // common
        self.den = bottom // common

    def show(self):
        """Prints the fraction data type as is"""
        self.simplify()
        print(self.num, "/", self.den)

    def simplify(self):
        """Simplifies the fraction for printing"""
        common = gcd(self.num, self.den)
        self.num = self.num // common
        self.den = self.den // common
        return self.num, self.den

    def __str__(self):
        """Converts the fraction data type to string"""
        return str(self.num) + "/" + str(self.den)

    def __repr__(self):
        """Prints an unambiguous string describing the object"""
        print('Fraction({0}, {1})'.format(self.num, self.den))

    def __add__(self, otherfraction):
        """Adds two fractions together"""
        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)

    def __radd__(self, otherfraction):
        """Implements reverse addition for fraction class"""
        if otherfraction == 0:
            return self
        else:
            self.__add__(otherfraction)

    def __iadd__(self, other):
        """Implements incrimental addition for fraction class"""
        self.num = self.num * other.den + self.den * other.num
        self.den = self.den * other.den
        return self

    def __sub__(self, otherfraction):
        """Subtracts one fraction from another"""
        newnum = self.num * otherfraction.den - self.den * otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)

    def __mul__(self, otherfraction):
        """Multiplying one fraction by another"""
        newnum = self.num * otherfraction.num
        newden = self.den * otherfraction.den

        return Fraction(newnum, newden)

    def __truediv__(self, otherfraction):
        """Divides one fraction by another"""
        newnum = self.num * otherfraction.den
        newden = self.den * otherfraction.num

        return Fraction(newnum, newden)

    def __eq__(self, other):
        """Determines whether fractions are equal by value"""
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum == secondnum

    def __ne__(self, other):
        """Returns a bool for if first fraction != second"""
        firstnum = self.num * other.den
        secondnum = other.num * self.den

        return firstnum != secondnum

    def __gt__(self, other):
        """Returns a bool for if first fraction if > second"""
        test1 = self.num / self.den
        test2 = other.num / other.den

        return test1 > test2

    def __ge__(self, other):
        """Returns a bool for if first fraction is >= second"""
        test1 = self.num / self.den
        test2 = other.num / other.den

        return test1 >= test2

    def __lt__(self, other):
        """Returns a bool for if second fraction is < second"""
        test1 = self.num / self.den
        test2 = other.num / other.den

        return test1 < test2

    def __le__(self, other):
        """Returns a bool for if first fraction is <= second"""
        test1 = self.num / self.den
        test2 = other.num / other.den

        return test1 <= test2

    def getNum(self):
        print("The fraction's numerator is " + str(self.num))

    def getDen(self):
        print("The fraction's denominator is " + str(self.den))


def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


test_fract1 = Fraction(3, 5)
test_fract2 = Fraction(4, 5)

print(test_fract2.__gt__(test_fract1))
print(test_fract1.__lt__(test_fract2))

print(test_fract1 + Fraction(1, 5))

test_fract1 += Fraction(1, 5)


test_fract1.show()
test_fract1.__str__()
test_fract1.__repr__()
