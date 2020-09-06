"""The class and functions for representing Polynomials"""

import itertools

def strip_list(xs, e):
    p = len(xs) - 1
    while p >= 0 and xs[p] == e:
        p -= 1
    return xs[:p+1]

class Polynomial:
    @classmethod
    def _single_term(cls, points, i):
        the_term = Polynomial([1.])
        xi, yi = points[i]

        for j, p in enumerate(points):
            if j == i:
                continue

            xj = p[0]
            the_term = the_term * Polynomial([-xj / (xi - xj), 1.0 / (xi - xj)])
        return the_term * Polynomial([yi])

    @classmethod
    def interpolating(cls, points):
        """Construct the interpolating polynomial for
        points, which is an iterable of (x, y) tuples"""
        if not points:
            raise ValueError('Must provide at least one point.')

        x_values = [p[0] for p in points]
        if len(set(x_values)) < len(x_values):
            raise ValueError('Not all x values are distinct.')

        terms = [Polynomial._single_term(points, i) for i in range(len(points))]
        return sum(terms, ZERO)

    def __init__(self, coefficients):
        self._coefficients = strip_list(coefficients, 0)
        if not self._coefficients:
            self._coefficients = [0]

    def eval_at(self, x):
        """Evaluate at x using Horner's method"""
        total = 0
        for e in reversed(self._coefficients):
            total = total*x + e
        return total

    def add(self, other):
        new_coeffs = [sum(pair) for pair in itertools.zip_longest(self, other, fillvalue=0)]
        return Polynomial(new_coeffs)

    def sub(self, other):
        return self.add(self, -other)

    def multiply(self, other):
        new_coefficients = [0] * (len(self) + len(other) - 1)
        for i, a in enumerate(self):
            for j, b in enumerate(other):
                new_coefficients[i+j] += a*b

        return Polynomial(strip_list(new_coefficients, 0))

    def len(self):
        return len(self._coefficients)

    def coefficients(self):
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
        return Polynomial([-c for c in self._coefficients])

    def __add__(self, other):
        return self.add(other)

    def __call__(self, x):
        return self.eval_at(x)

ZERO = Polynomial([])
