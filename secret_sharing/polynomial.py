"""The class and functions for representing Modular Polynomials"""

import itertools

from mod import Mod

def extended_gcd(a, b):
    """Euclids extended gcd algorithm."""
    x = 0
    y = 1
    last_x = 1
    last_y = 0

    while b != 0:
        quot = a // b
        a, b = b, a % b
        x, last_x = last_x - quot * x, x
        y, last_y = last_y - quot * y, y
    return last_x, last_y

def modular_div(a, b, p):
    """Modular division of a and b mod p,
    using the modular multiplicative inverse."""
    inv, _ = extended_gcd(b, p)
    return a * inv

def strip_list(xs, e):
    """Get rid of all rightmost 'e' in
    the given list."""
    p = len(xs) - 1
    while p >= 0 and xs[p] == e:
        p -= 1
    return xs[:p+1]

class ModPolynomial:
    """A polynomial constructed and evaluated mod p."""
    @classmethod
    def _single_term(cls, points, i, modulus):
        """Get the i-th term of the lagrange polynomial for the given points (mod p)."""
        the_term = ModPolynomial([1], modulus)
        xi, yi = points[i]

        for j, p in enumerate(points):
            if j == i:
                continue

            xj = p[0]
            # The coefficients are wrapped in the mod.Mod
            # class so we don't have to put '%' everywhere
            t0 = modular_div(-xj, xi - xj, modulus)
            t1 = modular_div(1, xi - xj, modulus)
            the_term = the_term * ModPolynomial([t0, t1], modulus)
        return the_term * ModPolynomial([Mod(yi, modulus)], modulus)

    @classmethod
    def interpolating(cls, points, modulus):
        """Construct the interpolating polynomial for
        points, which is an iterable of (x, y) tuples."""
        if not points:
            raise ValueError('Must provide at least one point.')

        x_values = [p[0] for p in points]
        if len(set(x_values)) < len(x_values):
            raise ValueError('Not all x values are distinct.')

        terms = [ModPolynomial._single_term(points, i, modulus) for i in range(len(points))]
        return sum(terms, ModPolynomial([], modulus))

    def __init__(self, coefficients, modulus):
        self.modulus = modulus
        coefficients = strip_list(coefficients, 0)
        if not coefficients:
            self._coefficients = [Mod(0, self.modulus)]
        else:
            self._coefficients = [Mod(c, self.modulus) for c in coefficients]

    def eval_at(self, x):
        """Evaluate at x using Horner's method"""
        x = Mod(x, self.modulus)
        total = Mod(0, self.modulus)
        for e in reversed(self._coefficients):
            total = total*x + e
        return int(total)

    def add(self, other):
        """Add two polynomials."""
        new_coeffs = [sum(p) for p in itertools.zip_longest(self, other, fillvalue=0)]
        return ModPolynomial(new_coeffs, self.modulus)

    def sub(self, other):
        """Subtract two polynomials."""
        return self.add(-other)

    def multiply(self, other):
        """Multiply two polynomials."""
        new_coefficients = [0] * (len(self) + len(other) - 1)
        for i, a in enumerate(self):
            for j, b in enumerate(other):
                new_coefficients[i+j] += a*b

        stripped = strip_list(new_coefficients, 0)
        return ModPolynomial(stripped, self.modulus)

    def len(self):
        """Return the length, which is the polynomials degree + 1"""
        return len(self._coefficients)

    def coefficients(self):
        """Return a list of the polynomials coefficients."""
        return list(self._coefficients)

    def __iter__(self):
        return iter(self._coefficients)

    def __len__(self):
        return self.len()

    def __mul__(self, other):
        return self.multiply(other)

    def __sub__(self, other):
        return self.sub(other)

    def __neg__(self):
        return ModPolynomial([-c for c in self._coefficients], self.modulus)

    def __add__(self, other):
        return self.add(other)

    def __call__(self, x):
        return self.eval_at(x)
