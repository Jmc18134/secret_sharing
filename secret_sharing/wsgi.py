from whitenoise import WhiteNoise

from secret_sharing import create_app

app = create_app()
app.wsgi_app = WhiteNoise(app.wsgi_app, root='static/')
