import functools
import secrets

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.exceptions import abort

from secret_sharing.polynomial import ModPolynomial

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

    error = ''
    if not (n and k and secret):
        error = 'All fields must be filled in!'
    elif n < k:
        error = 'N must be less than K!'

    try:
        n = int(n)
        k = int(k)
        secret = int(secret)
    except ValueError:
        error = 'N, K and Secret must be integers!'
    else:
        if n < 0 or k < 0 or secret < 0:
            error = 'All inputs must be greater than 0!'
        elif n < k:
            error = 'N must be >= K!'

    if error:
        flash(error)
        return redirect(url_for('encode.encode_secret'))

    # Get a prime larger than the secret and the number of shares
    prime = get_prime(max(n,k))
    # Generate random coefficients less than the prime modulus
    coefficients = [secrets.randbelow(prime) for _ in range(k-1)]
    coefficients.insert(0, secret)

    f = ModPolynomial(coefficients, prime)
    # Generate a share (x, f(x)) evaluated mod p for each n
    shares = [(x, f(x)) for x in range(1, n+1)]
    return render_template('encoder_results.html', shares=shares, prime=prime, n=n, k=k)
