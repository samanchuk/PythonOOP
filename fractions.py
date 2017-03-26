class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den
        if den == 0:
            print('Denominator should be more than 0')
            return None
        elif den < 0:
            self.den = abs(den)

    def get_num(self):
        return self.num

    def get_den(self):
        return self.den

    def get_real(self):
        if self.num // self.den > 0:
            return self.num // self.den
        else:
            return 0

    def to_float(self):
        return float(self.num / self.den)

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __repr__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        if isinstance(other, float):
            return self.to_float() + other
        else:
            new_num = self.num * other.den + self.den * other.num
            new_den = self.den * other.den
            return Fraction(new_num, new_den)

    def __sub__(self, other):
        if isinstance(other, float):
            return self.to_float() - other
        else:
            num_res = self.num * other.den - self.den * other.num
            den_res = self.den * other.den
            return Fraction(num_res, den_res)

    def __mul__(self, other):
        if isinstance(other, float):
            return self.to_float() * other
        else:
            num_res = self.num * other.num
            den_res = self.den * other.den
            return Fraction(num_res, den_res)

    def __truediv__(self, other):
        if isinstance(other, float):
            return self.to_float() / other
        else:
            num_res = self.num * other.den
            den_res = self.den * other.num
            return Fraction(num_res, den_res)

    def __eq__(self, other):
        return True if self.num * other.den == self.den * other.num else False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        num_res = self.num * other.den
        den_res = other.num * self.den
        return num_res < den_res

    def __gt__(self, other):
        return not self.__eq__(other)



fr1 = Fraction(1, 5)
fr2 = Fraction(2, 7)
fr3 = Fraction(2, 10)

print(fr1 + fr2)
print(fr1 - fr2)
print(fr1 * fr2)
print(fr1 / fr2)
print(fr1 == fr3)
print(fr1 > fr2)
print(fr1 + 5.8686)

