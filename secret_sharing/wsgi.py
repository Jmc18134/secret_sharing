from whitenoise import Whitenoise

from secret_sharing import create_app

app = create_app()
app.wsgi_app = Whitenoise(app.wsgi_app, root='static/')
