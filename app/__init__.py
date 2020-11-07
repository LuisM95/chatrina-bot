from flask import Flask
from flask_bootstrap import Bootstrap
 
app = Flask(__name__)  #creamos la instancia de aplicacion
bootstrap = Bootstrap()

from .views import page

def create_app(config):
    #creando app
    app.config.from_object(config)

    bootstrap.init_app(app)

    app.register_blueprint(page)
    return app