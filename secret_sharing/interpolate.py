import functools
import secrets

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.exceptions import abort

from secret_sharing.polynomial import Polynomial

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

    error = ''
    if not points:
        error = 'You must supply at least one point.'

    parsed = [pair.split(',') for pair in points.split(' ')]
    try:
        coords = [(int(a), int(b)) for (a, b) in parsed]
    except ValueError:
        error = 'Invalid values for coordinates.'
    else:
        xs = [a for a, b in coords]
        if not is_ascending(xs):
            error = 'X values must be ascending.'

    if error:
        flash(error)
        return redirect(url_for('interp.interpolate'))
    return render_template('interp_eval.html')
