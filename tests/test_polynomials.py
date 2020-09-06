from secret_sharing.polynomial import *

import pytest

@pytest.mark.parametrize("coefficients,x,expected", 
        [
            ([42, 1, 1, 1], 0, 42),
            ([1,2,3], 2, 17),
            ([0, 0, 0], 1, 0),
            ([1, 2, -5, -6], 2, -63),
            ([], 99, 0)
        ])
def test_evaluation(coefficients, x, expected):
    tester = Polynomial(coefficients)
    assert tester.eval_at(x) == expected

@pytest.mark.parametrize("points", [
    [(0.0, 0.0)],
    [(0.0, 0.0), (1.0, 1.0)],
    [(2.0, 2.0), (4.0, 1.0), (5.0, 3.0)],
    ])
def test_interpolation(points):
    tester = Polynomial.interpolating(points)
    for (x,y) in points:
        assert tester(x) == pytest.approx(y)

@pytest.mark.parametrize("first,second,result",
        [
            ([1, 1, 1], [1, 1, 1], [2, 2, 2]),
            ([1, 1, 1], [1, 1, 1, 1], [2, 2, 2, 1]),
            ([1, 1, 1], [1, -1, 1], [2, 0, 2]),
            ([0], [1, 1, 1], [1, 1, 1]),
            ([0], [0], [0]),
        ])
def test_addition(first, second, result):
    a = Polynomial(first)
    b = Polynomial(second)
    assert (a + b).coefficients() == result

@pytest.mark.parametrize("xs,expected",
        [
            ([1, 2, 3, 0, 0], [1, 2, 3]),
            ([1, 2, 3], [1, 2, 3]),
            ([0, 0, 0], [])
        ])
def test_list_strip(xs, expected):
    assert strip_list(xs, 0) == expected
