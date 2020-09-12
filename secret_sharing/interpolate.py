import functools
import secrets

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.exceptions import abort

from secret_sharing.polynomial import Polynomial

bp = Blueprint('interp', __name__, url_prefix='/interpolator')

@bp.route('/', methods=("GET", "POST"))
def interpolate():
    return render_template('interpolate.html')

@bp.route('/res', methods=("GET", "POST"))
def res():
    return render_template('interpolate.html')
