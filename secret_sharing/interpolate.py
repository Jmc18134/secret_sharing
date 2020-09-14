import functools
import secrets

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.exceptions import abort

from secret_sharing.polynomial import ModPolynomial

bp = Blueprint('interp', __name__, url_prefix='/interpolator')

def is_ascending(xs):
    for i in range(1, len(xs)):
        if xs[i] < xs[i-1]:
            return False
    return True

@bp.route('/', methods=("GET", "POST"))
def interpolate():
    return render_template('interpolate.html')

@bp.route('/eval', methods=("POST",))
def evaluate():
    points = request.form['points']
    modulus = request.form['modulus']
    x = request.form['x-val']

    # Lots of validation

    # Points must be a space-separated list of points x,y - i.e '3,4 5,6 9,2'
    # The x values of the points must be increasing, and the modulus (if one is supplied)
    # must be greater than or equal to one

    error = ''
    if not (points or x or modulus):
        error = 'All fields must be filled in.'

    parsed = [pair.split(',') for pair in points.split(' ')]
    try:
        coords = [(int(a), int(b)) for (a, b) in parsed]
        x = int(x)
        modulus = int(modulus)
    except ValueError:
        error = 'Invalid values. Please check your input.'
    else:
        xs = [a for a, b in coords]
        if not is_ascending(xs):
            error = 'X values must be ascending.'
        if modulus < 1:
            error = 'The modulus cannot be less than 1.'

    if error:
        flash(error)
        return redirect(url_for('interp.interpolate'))

    # Validation over, real work now

    # Generate the interpolating polynomial for the supplied coords,
    # And evaluate it at the given x and computing with the given modulus
    lagrange = ModPolynomial.interpolating(coords, modulus)
    result = lagrange(x)

    # The template needs the first (x-less) coefficient of the polynomial
    # and then the rest of the coefficients as a list
    # They need to be converted from mod.Mod to regular ints
    coef = [int(c) for c in lagrange.coefficients()]
    base, remaining = coef[0], coef[1:]

    return render_template('interp_eval.html', n=len(coords), x=x, base=base,
            modulus=modulus, answer=result, polynomial=remaining)
