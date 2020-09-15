from secret_sharing.polynomial import *

import pytest

@pytest.mark.parametrize("coefficients,mod,x,expected", 
        [
            ([42,1,1,1], 50, 0, 42),
            ([1,2,3], 20, 2, 17),
            ([0, 2, 3], 7, 9, 2),
            ([1, 0, 0, 1], 6, 3, 4),
            ([0, 0, 0], 10, 0, 0),
            ([1, 2, -5, -6], 32, 2, 1),
            ([], 99, 50, 0)
        ])
def test_evaluation(coefficients, mod, x, expected):
    tester = ModPolynomial(coefficients, mod)
    assert tester(x) == expected

@pytest.mark.parametrize("first,second,mod,result",
        [
            ([1, 1, 1], [1, 1, 1], 3, [2, 2, 2]),
            ([1, 1, 1], [1, 1, 1, 1], 3, [2, 2, 2, 1]),
            ([1, 1, 1], [1, -2, 1], 7, [2, 6, 2]),
            ([0], [1, 1, 1], 2, [1, 1, 1]),
            ([0], [0], 2, [0]),
        ])
def test_addition(first, second, mod, result):
    a = ModPolynomial(first, mod)
    b = ModPolynomial(second, mod)
    assert (a + b).coefficients() == result

@pytest.mark.parametrize("xs,expected",
        [
            ([1, 2, 3, 0, 0], [1, 2, 3]),
            ([1, 2, 3], [1, 2, 3]),
            ([0, 0, 0], [])
        ])
def test_list_strip(xs, expected):
    assert strip_list(xs, 0) == expected

@pytest.mark.parametrize("first,second,mod,result",
        [
            ([1, 1, 1], [1, 1, 1], 2, [0]),
            ([1, 1, 1], [2, 2, 2], 14, [13, 13, 13]),
            ([1, 1, 1], [1, 1, 1, 2], 7, [0, 0, 0, 5]),
            ([0], [0], 3, [0]),
        ])
def test_subtraction(first, second, mod, result):
    a = ModPolynomial(first, mod)
    b = ModPolynomial(second, mod)
    assert (a - b).coefficients() == result

@pytest.mark.parametrize("ys,mod,result",
        [
            ([(1,6), (2, 2), (3, 6)], 11, 7),
            ([(1,10), (2, 5), (3, 8)], 13, 10),
            ([(1, 145), (2, 85), (3, 37)], 197, 20),
            ([(1, 39), (2, 36), (3, 13), (4, 40), (5,39)], 41, 9)
        ])
def test_secretfinding(ys, mod, result):
    poly = ModPolynomial.interpolating(ys, mod)
    assert poly(0) == result
