#!/usr/bin/env python
"""complex_numbers.py

Show addition, multiplication, negation, and inversion of
complex numbers in separate functions."""

class Complex:
    def __init__(self, real, i):
        self.real = (float)(real)
        self.i = (float)(i)

    def __str__(self):
        if self.i >= 0:
            return "({} + {}i)".format(self.real, self.i)
        else:
            return "({} - {}i)".format(self.real, -1 * self.i)

    def add(self, c):
        if isinstance(c, Complex):
            r = self.real + c.real
            i = self.i + c.i
        else:
            r = self.real + c
            i = self.i
        result = Complex(r, i)
        return result

    def subtract(self, c):
        if isinstance(c, Complex):
            r = self.real - c.real
            i = self.i - c.i
        else:
            r = self.real - c
            i = self.i
        result = Complex(r, i)
        return result

    def negation(self):
        return Complex(-self.real, -self.i)

    def multiply(self, m):
        if isinstance(m, Complex):
            c1 = m.multiply(self.real)
            c2_r = -1 * m.i * self.i
            c2_i = m.real * self.i
            r = c1.real + c2_r
            i = c1.i + c2_i
            result = Complex(r, i)
        else:
            r = self.real * m
            i = self.i * m
            result = Complex(r, i)
        return result

    def conjugate(self):
        return Complex(self.real, -self.i)

    def divide(self, m):
        if isinstance(m, Complex):
            con = m.conjugate()
            numerator = self.multiply(con)
            # this operation cancels out the i part
            denominator = m.multiply(con)
            denominator = denominator.real
            return numerator.divide(denominator)
        else:
            return Complex(self.real / m, self.i / m)

a = Complex(4, 2)
b = Complex(2, 7)

print("a = {}".format(a))
print("b = {}".format(b))
print("a + b = {}".format(a.add(b)))
print("a - b = {}".format(a.subtract(b)))
print("5a = {}".format(a.multiply(5)))
print("a*b = {}".format(a.multiply(b)))
print("a.negation() = {}".format(a.negation()))
print("a.conjugate() = {}".format(b.conjugate()))
print("a/2 = {}".format(a.divide(2)))
print("a/b = {}".format(a.divide(b)))
