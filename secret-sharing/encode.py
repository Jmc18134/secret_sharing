import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.exceptions import abort

bp = Blueprint('encode', __name__)

@bp.route('/', methods=("GET", "POST"))
def encode_secret():
    if request.method == 'POST':
        n = request.form['shares']
        k = request.form['keys_required']
        secret = request.form['secret']

        error = None
        if not (n and k and secret):
            error = 'All fields must be filled in!'

        if error is not None:
            flash(error)
        return render_template('encode_secret.html')
    return render_template('encode_secret.html')
