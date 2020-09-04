import os

from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    # When deployed on heroku, this env will be set, otherwise we just use a dummy key
    secret = os.environ.get('FLASK_SECRET_KEY', 'dev')
    app.config.from_mapping(
        SECRET_KEY=secret,
    )

    # Eventually the app will be hosted on heroku's free tier,
    # so all this instance config stuff is just for dev and testing
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import encode
    app.register_blueprint(encode.bp)
    app.add_url_rule('/', endpoint='encode_secret')

    return app
