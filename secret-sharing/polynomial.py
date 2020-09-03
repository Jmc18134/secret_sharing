import itertools

def strip_list(xs):
    p = len(xs) - 1
    while xs[p] == 0:
        p -= 1
    return xs[:p+1]

class Polynomial:
    '''
    @classmethod
    def interpolate(cls, points):
    '''
    def __init__(self, coefficients):
        self.coefficients = strip_list(coefficients)

    def eval_at(x):
        total = 0
        for e in reversed(self.coefficients):
            total += total*x + e
        return total

    def add(other):
        new_coeffs = (a+b for (a,b) in itertools.zip_longest(
            self.coefficients, other.coefficents, fillvalue=0))
        return Polynomial(new_coeffs)

    def __add__(other):
        return self.add(self, other)

    def __call__(self, x):
        return self.eval_at(x)
