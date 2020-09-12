import functools
import secrets

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.exceptions import abort

from secret_sharing.polynomial import Polynomial

bp = Blueprint('encode', __name__)

def get_prime(n):
    return 197

@bp.route('/', methods=("GET",))
def encode_secret():
    return render_template('encode_secret.html')

@bp.route('/results', methods=("POST",))
def show_results():
    n = request.form['shares']
    k = request.form['keys_required']
    secret = request.form['secret']

    error = None
    if not (n and k and secret):
        error = 'All fields must be filled in!'

    n = int(n)
    k = int(k)
    secret = int(secret)

    if error is not None:
        flash(error)

    # Get a prime larger than the secret and the number of shares
    prime = get_prime(max(n,k))
    # Generate random coefficients less than the prime modulus
    coefficients = [secrets.randbelow(prime) for _ in range(k-1)]
    coefficients.insert(0, secret)

    poly = Polynomial(coefficients)

    # Generate a share (x, f(x)) evaluated mod p for each n
    shares = [(x, poly.eval_modp(x, prime)) for x in range(1, n+1)]
    return render_template('results.html', shares=shares, prime=prime, n=n, k=k)
